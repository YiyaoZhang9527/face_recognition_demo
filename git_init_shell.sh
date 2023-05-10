touch README.md
touch .gitignore
echo ".git_init_shell.sh" >> .gitignore
echo ".gitignore" >> .gitignore
git init
git add README.md
git add .
git commit -m "初始化"
git remote add origin git@github.com:YiyaoZhang9527/face_recognition_demo.git
git push -u origin master
