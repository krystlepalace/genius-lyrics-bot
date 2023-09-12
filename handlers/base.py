from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("This bot can search and send song lyrics from genius.com\nFor more help use /help")


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Use this bot in inline mode. Just type @geinus_lyrics_bot <song name> and results will appear soon!")