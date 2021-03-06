# Spin lifetime analysis

[![MIT License](https://img.shields.io/github/license/evansosenko/spin-lifetime-analysis.svg)](./LICENSE.txt)

## Requirements

- [Python 3](http://www.python.org/)
  with [pip](http://www.pip-installer.org/).

## Setup

Install the required Python packages with

```
$ pip install -r requirements.txt
```

### Reproducible requirements

The `requirements.txt` file uses major version semver constraints.
To install strict package dependency versions, use

```
$ pip install -r requirements.txt.lock
```

Update the lock file to match your environment with

```
$ pip freeze -r requirements.txt > requirements.txt.lock
```

### Setup troubleshooting

This is tested with Python 3.5.1 on 64-bit Linux
using an isolated Python Virtual Environment.

Running on OS X or Windows may require more preparation
then the single pip install command above.

Installing Python packages globally with `sudo pip` is not recommended.

Always keep pip updated first with

```
$ pip install --update pip
```

If pip is unable to compile the C extensions required by numpy, etc.,
you generally have two options:

  - Install NumPy and other core SciPy packages via your package manager.
    Then, install the other requirements normally at the user-level with pip.
    If using virtual environments with this method,
    make sure the environment is created with `--system-site-packages`.

  - Install a Python distribution such as [Anaconda]
    that bundles these dependncies and provides tools for
    managing Python environments.

To use `make` on OS X, install [Xcode], the Apple developer tools.
For Windows, download [Make for Windows] and place `make.exe` in your PATH
(or in the project root).

[Anaconda]: https://www.continuum.io/anaconda
[Make for Windows]: http://gnuwin32.sourceforge.net/packages/make.htm
[Xcode]: https://developer.apple.com/xcode/

## Usage

Execute the analysis with

```
$ make
```

Output will be saved in the `build` directory.

Python output will be redirected to `stdout.log`
and errors to `stderr.log`.

Remove the build and logs with

```
$ make clean
```

Serve the build directory from a local http server on port `8000` with

```
$ make serve
```

## Viewing fits with Fitalyzer.

After generating fits with `make`, run `make serve` and load
[io.evansosenko.com/fitalyzer/?firebase=spin-lifetime&port=8000&path=/fitalyzer](http://io.evansosenko.com/fitalyzer/?firebase=spin-lifetime&port=8000&path=/fitalyzer).

Note: you must visit [https://localhost:8000](https://localhost:8000)
in your browser and accept the SSL certificate for this to work.

## License

This code is licensed under the MIT license
with the exception of any files under the path `data/PhysRevLett.105.167202`.

All files under the path `data/PhysRevLett.105.167202`
were compiled from data presented in:

> [Tunneling Spin Injection into Single Layer Graphene](http://link.aps.org/doi/10.1103/PhysRevLett.105.167202).
> Wei Han, K. Pi, K. M. McCreary, Yan Li, Jared J. I. Wong, Adrian G. Swartz, and Roland K. Kawakami, Phys. Rev. Lett. 105, 167202 (2010)

This data was used with permission and is available for download:
[Joint Laboratory for Spintronics Research, Department of Physics and Astronomy, University of California, Riverside](http://physics.ucr.edu/~kawakami/jlsrPublications.html).

## Warranty

This software is provided "as is" and without any express or
implied warranties, including, without limitation, the implied
warranties of merchantibility and fitness for a particular
purpose.
