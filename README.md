<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=320&color=0C134F&text=ORBITAL%20TRANSMISSION&fontColor=00F5FF&fontSize=60&animation=twinkling&stroke=7C00FF&strokeWidth=1.4&desc=its-2006-batman%20%7C%20Space%20Ops%20Full-Stack%20Developer&descAlignY=70&fontAlignY=42" width="100%" alt="Cosmic banner" />
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=26&duration=2800&pause=700&color=39FF14&center=true&vCenter=true&width=900&lines=Mission+Control+Online;Deploying+Java+Backends+and+Reactive+Web+Nebulas;Automation+Pilots+for+Cyberpunk+UX;Hello+Earthian%2C+Welcome+Aboard" alt="mission typing banner" />
</div>

## Mission Brief

<div align="center">

![visitors](https://komarev.com/ghpvc/?username=its-2006-batman&style=for-the-badge&label=STAR+VISITORS&color=00F5FF&labelColor=050816)
![followers](https://img.shields.io/github/followers/its-2006-batman?style=for-the-badge&logo=github&label=CREW&color=FF00E5&labelColor=050816)
![status](https://img.shields.io/badge/STATUS-ORBITING-39FF14?style=for-the-badge&labelColor=050816)
![mode](https://img.shields.io/badge/MODE-SPACE_THEME_ULTRA-8A2BE2?style=for-the-badge&labelColor=050816)

</div>

- building cinematic web systems with Spring Boot cores, GSAP choreographies, and neon UI shaders
- fusing automation pilots (GitHub Actions, browser bots) with storytelling dashboards
- remote-friendly from Earth orbit, collaborating via [github.com/its-2006-batman](https://github.com/its-2006-batman)

```javascript
const missionControl = {
  codename: "its-2006-batman",
  stack: ["Java", "Spring", "JavaScript", "GSAP", "Three.js", "MV3"],
  focus: ["Creative Frontend", "Java Backend", "Browser Automation"],
  status: "Deploying space-grade user journeys",
  comms: "Hello Earthian"
};
```

## Payload & Systems

<div align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,js,ts,html,css,mysql,git,github,vscode&theme=dark" alt="primary stack" />
</div>

<div align="center">
  <img src="https://img.shields.io/badge/GSAP-88CE02?style=for-the-badge&logo=greensock&logoColor=111" alt="GSAP" />
  <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=fff" alt="Three.js" />
  <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=fff" alt="jQuery" />
  <img src="https://img.shields.io/badge/Chrome_Extension_API-MV3-4285F4?style=for-the-badge&logo=googlechrome&logoColor=fff" alt="Chrome Extension API" />
</div>

## Telemetry

<div align="center">
  <img height="180" src="https://github-readme-stats.vercel.app/api?username=its-2006-batman&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=percentile&include_all_commits=true" alt="GitHub stats" />
  <img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=its-2006-batman&layout=donut&theme=tokyonight&hide_border=true&langs_count=8" alt="Top languages" />
</div>

<div align="center">
  <img width="98%" src="https://streak-stats.demolab.com?user=its-2006-batman&theme=tokyonight&hide_border=true&mode=weekly" alt="activity streak" />
</div>

### WakaTime Feed

WakaTime stats auto-sync after the workflow run so the cockpit stays fresh.

```
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

### Contribution Constellation

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/its-2006-batman/its-2006-batman/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/its-2006-batman/its-2006-batman/output/github-snake.svg" />
    <img alt="orbit snake" src="https://raw.githubusercontent.com/its-2006-batman/its-2006-batman/output/github-snake.svg" width="100%" />
  </picture>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=130&section=footer&color=0C134F&textColor=00F5FF&animation=twinkling" width="100%" alt="footer galaxy" />
</div>

## Launch Automations

```yaml
name: Neon Automation

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  snake:
    name: Generate Snake
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Generate contribution snake
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg?palette=github-light
            dist/github-snake-dark.svg?palette=github-dark

      - name: Push snake to output branch
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  wakatime:
    name: Update WakaTime In README
    runs-on: ubuntu-latest
    needs: snake
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Update README with WakaTime stats
        uses: anmol098/waka-readme-stats@master
        with:
          WAKATIME_API_KEY: ${{ waka_474722ae-f4de-4da1-b9fc-6bb1703e7ed3 }}
          GH_TOKEN: ${{ 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 }}
          SHOW_TOTAL_CODE_TIME: "true"
          SHOW_PROFILE_VIEWS: "false"
          SHOW_SHORT_INFO: "true"
          SHOW_LINES_OF_CODE: "true"
          SHOW_LOC_CHART: "false"
          SHOW_PROJECTS: "true"
          SHOW_EDITORS: "true"
          SHOW_OS: "true"
          SHOW_LANGUAGE: "true"
          SHOW_DAYS_OF_WEEK: "true"
          SHOW_TIMEZONE: "false"
          UPDATED_DATE_FORMAT: "ddd, DD MMM YYYY"
          COMMIT_BY_ME: "false"
          REPOSITORY: ${{ github.repository }}
```


