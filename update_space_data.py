"""
🚀 Space & Tech Data Scraper for GitHub Profile
================================================
This script fetches real-time space and tech data to keep your README fresh.

Data Sources:
- SpaceX API: Latest launch data
- NASA API: Astronomy Picture of the Day  
- ISS Tracking API: Current ISS position
- HackerNews API: Trending tech headlines
- GitHub API: Trending repositories

Usage:
    python update_space_data.py
    
Setup:
    pip install requests beautifulsoup4 python-dotenv
"""

import requests
import json
from datetime import datetime, timezone
from typing import Dict, List, Optional
import os

LIVE_DATA_START = "<!-- LIVE_DATA_START -->"
LIVE_DATA_END = "<!-- LIVE_DATA_END -->"

class SpaceTechScraper:
    def __init__(self):
        self.data = {}
        self.timestamp = datetime.now(timezone.utc).isoformat()
        
    def fetch_spacex_latest_launch(self) -> Optional[Dict]:
        """Fetch latest SpaceX launch information"""
        try:
            url = "https://api.spacexdata.com/v5/launches/latest"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, dict):
                raise ValueError("Unexpected SpaceX API response format")
            rocket = data.get('rocket')
            rocket_name = rocket.get('name', 'Unknown') if isinstance(rocket, dict) else (rocket or 'Unknown')
            details = (data.get('details') or 'No details available')[:200]
            
            return {
                'mission': data.get('name', 'Unknown'),
                'rocket': rocket_name,
                'date': data.get('date_utc', 'Unknown'),
                'success': data.get('success', None),
                'details': details,
                'flight_number': data.get('flight_number', 0)
            }
        except Exception as e:
            print(f"❌ SpaceX API Error: {e}")
            return None
    
    def fetch_nasa_apod(self, api_key: str = "DEMO_KEY") -> Optional[Dict]:
        """Fetch NASA Astronomy Picture of the Day"""
        try:
            url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            return {
                'title': data.get('title', 'Unknown'),
                'date': data.get('date', 'Unknown'),
                'explanation': data.get('explanation', '')[:300] + '...',
                'url': data.get('url', ''),
                'media_type': data.get('media_type', 'image')
            }
        except Exception as e:
            print(f"❌ NASA API Error: {e}")
            return None
    
    def fetch_iss_position(self) -> Optional[Dict]:
        """Fetch current ISS location"""
        try:
            url = "http://api.open-notify.org/iss-now.json"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            position = data.get('iss_position', {})
            lat = float(position.get('latitude', 0))
            lon = float(position.get('longitude', 0))
            
            # Determine hemisphere
            lat_dir = 'N' if lat >= 0 else 'S'
            lon_dir = 'E' if lon >= 0 else 'W'
            
            return {
                'latitude': f"{abs(lat):.2f}°{lat_dir}",
                'longitude': f"{abs(lon):.2f}°{lon_dir}",
                'timestamp': datetime.fromtimestamp(data.get('timestamp', 0), timezone.utc).isoformat(),
                'velocity': '~27,600 km/h',  # ISS orbital velocity
                'altitude': '~408 km'         # Average ISS altitude
            }
        except Exception as e:
            print(f"❌ ISS Tracking Error: {e}")
            return None
    
    def fetch_tech_headlines(self, count: int = 5) -> List[Dict]:
        """Fetch top tech headlines from HackerNews"""
        try:
            # Get top story IDs
            url = "https://hacker-news.firebaseio.com/v0/topstories.json"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            story_ids = response.json()[:count]
            
            headlines = []
            for story_id in story_ids:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                story_response = requests.get(story_url, timeout=5)
                
                if story_response.status_code == 200:
                    story = story_response.json()
                    headlines.append({
                        'title': story.get('title', 'Unknown'),
                        'score': story.get('score', 0),
                        'url': story.get('url', f"https://news.ycombinator.com/item?id={story_id}"),
                        'time': datetime.fromtimestamp(story.get('time', 0)).isoformat()
                    })
            
            return headlines
        except Exception as e:
            print(f"❌ HackerNews API Error: {e}")
            return []
    
    def fetch_github_trending(self, language: str = "javascript") -> List[Dict]:
        """Fetch GitHub trending repositories"""
        try:
            # Note: GitHub's official trending requires scraping or unofficial APIs
            # Using GitHub's search API as alternative
            url = f"https://api.github.com/search/repositories"
            params = {
                'q': f'language:{language} stars:>1000',
                'sort': 'stars',
                'order': 'desc',
                'per_page': 5
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            repos = []
            for repo in data.get('items', [])[:5]:
                repos.append({
                    'name': repo.get('full_name', 'Unknown'),
                    'description': repo.get('description', 'No description')[:150],
                    'stars': repo.get('stargazers_count', 0),
                    'language': repo.get('language', 'Unknown'),
                    'url': repo.get('html_url', '')
                })
            
            return repos
        except Exception as e:
            print(f"❌ GitHub API Error: {e}")
            return []
    
    def generate_readme_section(self) -> str:
        """Generate markdown section with fetched data"""
        iss = self.data.get('iss_position') or {}
        spacex = self.data.get('spacex_launch') or {}
        
        section = f"""
## 🛸 [ LIVE SPACE DATA ]

```
╔════════════════════════════════════════════════════════════════╗
║  🛰️  ISS TRACKING - REAL-TIME POSITION                        ║
╠════════════════════════════════════════════════════════════════╣
║  📍 LATITUDE:  {iss.get('latitude', 'N/A'):<45} ║
║  📍 LONGITUDE: {iss.get('longitude', 'N/A'):<45} ║
║  ⚡ VELOCITY:  {iss.get('velocity', 'N/A'):<45} ║
║  🌍 ALTITUDE:  {iss.get('altitude', 'N/A'):<45} ║
║  ⏰ LAST UPDATE: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'):<42} ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║  🚀 LATEST SPACEX MISSION                                      ║
╠════════════════════════════════════════════════════════════════╣
║  MISSION: {spacex.get('mission', 'N/A'):<52} ║
║  STATUS:  {('✓ SUCCESS' if spacex.get('success') else '⚠ PENDING'):<52} ║
║  FLIGHT:  #{spacex.get('flight_number', 'N/A'):<51} ║
╚════════════════════════════════════════════════════════════════╝
```
"""
        return section
    
    def scrape_all(self):
        """Run all scrapers"""
        print("🚀 Initiating Space & Tech Data Scraping...")
        print("=" * 70)
        
        # SpaceX
        print("\n🛸 Fetching SpaceX data...")
        self.data['spacex_launch'] = self.fetch_spacex_latest_launch()
        
        # NASA
        print("🌌 Fetching NASA APOD...")
        self.data['nasa_apod'] = self.fetch_nasa_apod(os.getenv("NASA_API_KEY", "DEMO_KEY"))
        
        # ISS
        print("🛰️  Tracking ISS...")
        self.data['iss_position'] = self.fetch_iss_position()
        
        # Tech News
        print("💻 Fetching tech headlines...")
        self.data['tech_headlines'] = self.fetch_tech_headlines()
        
        # GitHub Trending
        print("⭐ Fetching GitHub trending...")
        self.data['github_trending'] = self.fetch_github_trending()
        
        self.data['last_updated'] = self.timestamp
        
        print("\n✓ Data collection complete!")
        print("=" * 70)
        
        return self.data
    
    def save_to_json(self, filename: str = "space_tech_data.json"):
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"✓ Data saved to {filename}")
    
    def update_readme(self, readme_path: str = "README.md"):
        """Update README with new data"""
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_section = self.generate_readme_section()

            if LIVE_DATA_START in content and LIVE_DATA_END in content:
                before = content.split(LIVE_DATA_START, 1)[0]
                after = content.split(LIVE_DATA_END, 1)[1]
                updated_content = (
                    f"{before}{LIVE_DATA_START}\n"
                    f"{new_section.strip()}\n"
                    f"{LIVE_DATA_END}{after}"
                )
                action = "updated"
            else:
                updated_content = (
                    f"{content.rstrip()}\n\n"
                    f"{LIVE_DATA_START}\n"
                    f"{new_section.strip()}\n"
                    f"{LIVE_DATA_END}\n"
                )
                action = "inserted"

            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"✓ README {action} with live space data")
            
        except Exception as e:
            print(f"❌ README update error: {e}")

def main():
    scraper = SpaceTechScraper()
    data = scraper.scrape_all()
    scraper.save_to_json()
    scraper.update_readme()
    
    # Print summary
    print("\n" + "="*70)
    print("📊 DATA SUMMARY:")
    print("="*70)
    
    if data.get('iss_position'):
        iss = data['iss_position']
        print(f"🛰️  ISS: {iss['latitude']}, {iss['longitude']}")
    
    if data.get('spacex_launch'):
        spacex = data['spacex_launch']
        print(f"🚀 SpaceX: {spacex['mission']} (Flight #{spacex['flight_number']})")
    
    if data.get('tech_headlines'):
        print(f"💻 Tech: {len(data['tech_headlines'])} headlines retrieved")
    
    print("="*70)

if __name__ == "__main__":
    main()
