from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0', proxies={'HTTPS': '81.171.24.199:3128'}).streams.get_highest_resolution().download('C:\\Users\\user\\Downloads')
