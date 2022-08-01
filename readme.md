# This is a readme file
This project was created to learn with a practical example of the CI/CD process.   The website is basic with simple text and an image, however it makes for a good base to learn the process.

The following build script, removes any docker container named wsite and then builds/re-builds the website docker container, it then runs it on port 82, creates a display  and then runs the python test, one complete it cleans up.

```bash
sudo docker rm -f wsite
sudo docker build /home/vagrant/projects/website/. -t test
sudo docker run --name wsite -it -p 82:80 -d test
export DISPLAY=:99
Xvfb :99 -ac -screen 0 1280x1024x24 &
python3 testsite.py
killall Xvfb
```

<img src="https://i.imgur.com/7FkVHgs.png" alt="python" title="CI/CD">

<img src="https://i.imgur.com/boPwKvU.png" alt="website" title="CI/CD">

