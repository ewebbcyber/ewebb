import os

UPLOAD_DIR = 'uploads'
FILES = sorted(f for f in os.listdir(UPLOAD_DIR) if not f.startswith('.'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Uploaded Files</title>
  <meta http-equiv="refresh" content="15" />
  <link rel="icon" type="image/x-icon" href="favicon.ico" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header>
    <img src="images/logo.png" alt="Logo" />
    <h1>Uploaded Files</h1>
  </header>
  <div class="content">
    <ul>\n""")

    for file in FILES:
        file_path = f"{UPLOAD_DIR}/{file}"
        f.write(f"""      <li class="file">
        <a href="{file_path}" target="_blank">{file}</a>
        <button class="copy-btn" onclick="copyToClipboard('{file_path}')">Copy Link</button>
      </li>\n""")

    f.write("""    </ul>
  </div>
  <script>
    function copyToClipboard(link) {
      const fullLink = `${location.origin}/${link}`;
      navigator.clipboard.writeText(fullLink).then(() => {
        alert('Link copied to clipboard!');
      }).catch(err => {
        console.error('Failed to copy: ', err);
      });
    }
  </script>
</body>
</html>""")
