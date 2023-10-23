---
layout: container
name:  "quay.io/biocontainers/chicagotools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chicagotools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chicagotools/container.yaml"
updated_at: "2023-10-23 02:36:25.296114"
latest: "1.2.0--2"
container_url: "https://biocontainers.pro/tools/chicagotools"
aliases:
 - "bam2chicago.sh"
 - "fitDistCurve.R"
 - "makeDesignFiles.py"
 - "makeNBaitsPerBinFile.py"
 - "makeNPerBinFile.py"
 - "makePeakMatrix.R"
 - "makeProxOEFile.py"
 - "runChicago.R"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "c89"
 - "c99"
versions:
 - "1.2.0--2"
description: "shpc-registry automated BioContainers addition for chicagotools"
config: {"url": "https://biocontainers.pro/tools/chicagotools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chicagotools", "latest": {"1.2.0--2": "sha256:a54128a8fb650b7d92dd95a9062bc032f5c95bda3ccf06ee2296c5b9595b7a08"}, "tags": {"1.2.0--2": "sha256:a54128a8fb650b7d92dd95a9062bc032f5c95bda3ccf06ee2296c5b9595b7a08"}, "docker": "quay.io/biocontainers/chicagotools", "aliases": {"bam2chicago.sh": "/usr/local/bin/bam2chicago.sh", "fitDistCurve.R": "/usr/local/bin/fitDistCurve.R", "makeDesignFiles.py": "/usr/local/bin/makeDesignFiles.py", "makeNBaitsPerBinFile.py": "/usr/local/bin/makeNBaitsPerBinFile.py", "makeNPerBinFile.py": "/usr/local/bin/makeNPerBinFile.py", "makePeakMatrix.R": "/usr/local/bin/makePeakMatrix.R", "makeProxOEFile.py": "/usr/local/bin/makeProxOEFile.py", "runChicago.R": "/usr/local/bin/runChicago.R", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chicagotools.
shpc-registry automated BioContainers addition for chicagotools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chicagotools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chicagotools:1.2.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chicagotools/1.2.0--2
$ module help quay.io/biocontainers/chicagotools/1.2.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chicagotools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chicagotools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chicagotools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chicagotools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chicagotools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chicagotools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2chicago.sh

```bash
$ singularity exec <container> /usr/local/bin/bam2chicago.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bam2chicago.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2chicago.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitDistCurve.R

```bash
$ singularity exec <container> /usr/local/bin/fitDistCurve.R
$ podman run --it --rm --entrypoint /usr/local/bin/fitDistCurve.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitDistCurve.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDesignFiles.py

```bash
$ singularity exec <container> /usr/local/bin/makeDesignFiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/makeDesignFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDesignFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeNBaitsPerBinFile.py

```bash
$ singularity exec <container> /usr/local/bin/makeNBaitsPerBinFile.py
$ podman run --it --rm --entrypoint /usr/local/bin/makeNBaitsPerBinFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeNBaitsPerBinFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeNPerBinFile.py

```bash
$ singularity exec <container> /usr/local/bin/makeNPerBinFile.py
$ podman run --it --rm --entrypoint /usr/local/bin/makeNPerBinFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeNPerBinFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makePeakMatrix.R

```bash
$ singularity exec <container> /usr/local/bin/makePeakMatrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/makePeakMatrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makePeakMatrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeProxOEFile.py

```bash
$ singularity exec <container> /usr/local/bin/makeProxOEFile.py
$ podman run --it --rm --entrypoint /usr/local/bin/makeProxOEFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeProxOEFile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runChicago.R

```bash
$ singularity exec <container> /usr/local/bin/runChicago.R
$ podman run --it --rm --entrypoint /usr/local/bin/runChicago.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runChicago.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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