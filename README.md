# 🎨 GitHub Activity Painter

The script allow "drawing" on GitHub activity chart (Contribution Graph) by creating empty commits on defined days.

## 🚀 How it works

Script reads pixel coordinates from text file and runs command `git commit` for each point, defines environment variables `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` on the go.

## 🛠 Get ready

1. **Create new empty repo** на GitHub.
1. **Clone it** locally:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
1. Create file `data.txt` with coordinates (format: week, day):
* x (week): 0..51
* y (day): 0(Sunday)..6(Saturday)

You can add comments after `#` and group pixels with `;`.

## 💻 Run
Start script and provide date of the first week.
```bash
python draw.py --start 2025-01-05
```
Pass parameters:
* `--start`: Start day in format YYYY-MM-DD.
* `--file`: (Optional) Path to file with data (`data.txt` by default).

After script run publish commits to GitHub:
```bash
git push origin main
```
