from config import FAILED
from youtubesearchpython.__future__ import VideosSearch
import aiohttp
from PIL import Image
from io import BytesIO

async def download_image(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.read()
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None
    
async def crop_to_16_9(image_data):
    try:
        with Image.open(BytesIO(image_data)) as img:
            width, height = img.size
            target_ratio = 16 / 9
            current_ratio = width / height
            
            if current_ratio > target_ratio:
                new_width = int(height * target_ratio)
                offset = (width - new_width) // 2
                img = img.crop((offset, 0, offset + new_width, height))
            elif current_ratio < target_ratio:
                new_height = int(width / target_ratio)
                offset = (height - new_height) // 2
                img = img.crop((0, offset, width, offset + new_height))
            
            output_buffer = BytesIO()
            img.save(output_buffer, format="JPEG")
            output_buffer.seek(0)
            return output_buffer.read()
    except Exception as e:
        print(f"Error cropping image: {e}")
        return None
    
async def gen_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
            thumbnail_url = thumbnail_url.replace("hqdefault", "maxresdefault")

            image_data = await download_image(thumbnail_url)
            if image_data:
                cropped_image = await crop_to_16_9(image_data)
                return cropped_image
        return FAILED
    except Exception as e:
        return FAILED

async def gen_qthumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
            thumbnail_url = thumbnail_url.replace("hqdefault", "maxresdefault")

            image_data = await download_image(thumbnail_url)
            if image_data:
                cropped_image = await crop_to_16_9(image_data)
                return cropped_image
        return FAILED
    except Exception as e:
        return FAILED