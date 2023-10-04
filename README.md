# FlameScope

![FlameScope](docs/screenshot-flamescope-02-annotated.png)

[![Gitter](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/flamescope)
[![TravisCI](https://travis-ci.com/Netflix/flamescope.svg)](https://travis-ci.com/Netflix/flamescope)
[![NetflixOSS Lifecycle](https://img.shields.io/osslifecycle/Netflix/flamescope.svg)]()
[![License](https://img.shields.io/github/license/Netflix/flamescope.svg)](http://www.apache.org/licenses/LICENSE-2.0)

FlameScope is a visualization tool for exploring different time ranges as Flame Graphs, allowing quick analysis of performance issues such as perturbations, variance, single-threaded execution, and more.

## Installation on Apple Silicon

The installation instructions in the main repository did not work on the M1 (neither Python, nor the frontend). For convenience, I built the frontend on a Linux machine and included them in this fork, so you don't have to worry about running `npm run webpack`. You just need to run the Python server. E2E, here's what it looks like:

```bash
git clone https://github.com/neilramaswamy/flamescope
cd flamescope

# Create a venv
python3 -m venv env
source ./env/bin/activate

# Apparently, this: https://github.com/Yelp/elastalert/issues/1927#issuecomment-549142662
brew install libmagic

pip3 install -r requirements.txt
python3 run.py
```

I'd like to port some of this to the main-repo, but I don't have time. If you'd like to help, please feel free to upstream my changes.


## The rest of the README

Please see the [original repo](https://github.com/Netflix/flamescope) for the reset of the README.

