import os
import asyncio
from dotenv import load_dotenv
from supabase import Client,create_client
from src.repository.usersrepository import UserRepository
from src.repository.SupabaseUserRepository import SupabaseUserRepository
from src.models.users import User


load_dotenv()

# Инициализация подключения к базе данных Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url,key)
table_name = "usersData"

users:UserRepository = SupabaseUserRepository(supabase)

def get_user_state_by_id(chat_id: int) -> str:
    try:
        user = users.get(chat_id)
        return user.user_state
    except Exception as e:
        print(f"Error retrieving user state for {chat_id}: {e}")
        return ""

def update_user_state_by_id(chat_id: int, state: str):
    try:
        user = users.get(chat_id)
        user.user_state = state
        users.set(user)
        print(f"Updated user state for {chat_id}: {state}")
    except Exception as e:
        print(f"Error updating user state for {chat_id}: {e}")


def delete_user_data_by_id(chat_id: int) -> str:
    try:
        chat_id_str = str(chat_id)
        result = supabase.table(table_name).delete().eq('chat_id', chat_id_str).execute()
        if result["error"]:
            print(f"Error deleting rows: {result['error']}")
        else:
            print(f"{result['count']} rows deleted")
    except Exception as e:
        print(f"Error delete user data: {chat_id}: {e}")


def get_user_info_by_id(chat_id:int ) -> User:
    try:
        user = users.get(chat_id)
        return user
    except Exception as e:
        print(f"Error get info about user: {chat_id}: {e}")

