import os
import subprocess
from rich.prompt import Prompt
from rich.progress import Progress
from rich import print
from urllib.parse import urlparse

def get_slug_from_url(url):
    try:
        parsed = urlparse(url)
        slug = parsed.path.strip("/").split("/")[-1]
        return slug or "video"
    except:
        return "video"

def ask_location():
    folder = Prompt.ask("[green]📁 Lokasi simpan (cth: /sdcard/Download)", default="/sdcard/Download")
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def ask_format():
    format_map = {
        "1": "mp4",
        "2": "mp3",
        "3": "m4a"
    }
    print("\n[cyan]🎞 Pilih format download:")
    print("[1] MP4 (video)")
    print("[2] MP3 (audio)")
    print("[3] M4A (audio)")
    choice = Prompt.ask("Masukkan nomor", choices=["1", "2", "3"], default="1")
    return format_map[choice]

def download_video(url, save_path, slug, format_choice):
    print(f"\n[green]🚀 Mendownload dari:[/green] {url}")
    output_template = os.path.join(save_path, f"{slug}.%(ext)s")

    format_flags = {
        "mp4": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "mp3": "bestaudio[ext=m4a]/bestaudio",
        "m4a": "bestaudio[ext=m4a]/bestaudio"
    }

    ytdlp_cmd = [
        "yt-dlp",
        "-f", format_flags.get(format_choice, "mp4"),
        "-o", output_template,
        url
    ]

    try:
        subprocess.run(ytdlp_cmd, check=True)
        print(f"\n[bold green]✅ Berhasil! File disimpan di {save_path}/{slug}[/bold green]\n")
    except subprocess.CalledProcessError:
        print("[yellow]⚠️ Gagal format utama, mencoba fallback format...[/yellow]")
        try:
            fallback_cmd = ["yt-dlp", "-f", "mp4", "-o", output_template, url]
            subprocess.run(fallback_cmd, check=True)
            print(f"\n[bold green]✅ Berhasil dengan fallback format! File di {save_path}/{slug}[/bold green]\n")
        except subprocess.CalledProcessError as e:
            print(f"[red]✗ Tetap gagal download: {e}[/red]")

def main():
    os.system("clear")
    print("[bold cyan]CYLNE DOWNLOADER[/bold cyan]")
    url = Prompt.ask("🔗 Masukkan URL video (TikTok/YouTube)")
    slug = Prompt.ask("📝 Nama file (tanpa ekstensi)", default=get_slug_from_url(url))
    save_path = ask_location()
    format_choice = ask_format()
    download_video(url, save_path, slug, format_choice)

if __name__ == "__main__":
    main()