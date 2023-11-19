---
layout: container
name:  "quay.io/biocontainers/jamm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jamm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jamm/container.yaml"
updated_at: "2023-11-19 02:37:16.955665"
latest: "1.0.8.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/jamm"
aliases:
 - "JAMM.sh"
 - "SignalGenerator.sh"
 - "bincalculator.r"
 - "peakfilter.pl"
 - "peakfinder.r"
 - "peakhelper.r"
 - "readshifter.pl"
 - "signalmaker.r"
 - "xcorr.r"
 - "xcorrhelper.r"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "perl5.32.0"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "streamzip"
versions:
 - "1.0.8.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for jamm"
config: {"url": "https://biocontainers.pro/tools/jamm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jamm", "latest": {"1.0.8.0--hdfd78af_1": "sha256:515a2fcf19f1976119cf8e26ecd0c9130a5303bbff9b79dcb038c31f05b46c7e"}, "tags": {"1.0.8.0--hdfd78af_1": "sha256:515a2fcf19f1976119cf8e26ecd0c9130a5303bbff9b79dcb038c31f05b46c7e"}, "docker": "quay.io/biocontainers/jamm", "aliases": {"JAMM.sh": "/usr/local/bin/JAMM.sh", "SignalGenerator.sh": "/usr/local/bin/SignalGenerator.sh", "bincalculator.r": "/usr/local/bin/bincalculator.r", "peakfilter.pl": "/usr/local/bin/peakfilter.pl", "peakfinder.r": "/usr/local/bin/peakfinder.r", "peakhelper.r": "/usr/local/bin/peakhelper.r", "readshifter.pl": "/usr/local/bin/readshifter.pl", "signalmaker.r": "/usr/local/bin/signalmaker.r", "xcorr.r": "/usr/local/bin/xcorr.r", "xcorrhelper.r": "/usr/local/bin/xcorrhelper.r", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "perl5.32.0": "/usr/local/bin/perl5.32.0", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jamm.
shpc-registry automated BioContainers addition for jamm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jamm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jamm:1.0.8.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jamm/1.0.8.0--hdfd78af_1
$ module help quay.io/biocontainers/jamm/1.0.8.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jamm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jamm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jamm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jamm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jamm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jamm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### JAMM.sh

```bash
$ singularity exec <container> /usr/local/bin/JAMM.sh
$ podman run --it --rm --entrypoint /usr/local/bin/JAMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JAMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SignalGenerator.sh

```bash
$ singularity exec <container> /usr/local/bin/SignalGenerator.sh
$ podman run --it --rm --entrypoint /usr/local/bin/SignalGenerator.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SignalGenerator.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bincalculator.r

```bash
$ singularity exec <container> /usr/local/bin/bincalculator.r
$ podman run --it --rm --entrypoint /usr/local/bin/bincalculator.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bincalculator.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakfilter.pl

```bash
$ singularity exec <container> /usr/local/bin/peakfilter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/peakfilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakfilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakfinder.r

```bash
$ singularity exec <container> /usr/local/bin/peakfinder.r
$ podman run --it --rm --entrypoint /usr/local/bin/peakfinder.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakfinder.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakhelper.r

```bash
$ singularity exec <container> /usr/local/bin/peakhelper.r
$ podman run --it --rm --entrypoint /usr/local/bin/peakhelper.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakhelper.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readshifter.pl

```bash
$ singularity exec <container> /usr/local/bin/readshifter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/readshifter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readshifter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### signalmaker.r

```bash
$ singularity exec <container> /usr/local/bin/signalmaker.r
$ podman run --it --rm --entrypoint /usr/local/bin/signalmaker.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/signalmaker.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcorr.r

```bash
$ singularity exec <container> /usr/local/bin/xcorr.r
$ podman run --it --rm --entrypoint /usr/local/bin/xcorr.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcorr.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcorrhelper.r

```bash
$ singularity exec <container> /usr/local/bin/xcorrhelper.r
$ podman run --it --rm --entrypoint /usr/local/bin/xcorrhelper.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcorrhelper.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)