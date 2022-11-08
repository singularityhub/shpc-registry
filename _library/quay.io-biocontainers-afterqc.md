---
layout: container
name:  "quay.io/biocontainers/afterqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/afterqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/afterqc/container.yaml"
updated_at: "2022-11-08 00:03:02.666992"
latest: "0.9.7--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/afterqc"
aliases:
 - "after.py"
 - "barcodeprocesser.py"
 - "bubbledetector.py"
 - "bubbleprocesser.py"
 - "circledetector.py"
 - "debubble.py"
 - "fastq.py"
 - "preprocesser.py"
 - "qcreporter.py"
 - "qualitycontrol.py"
 - "util.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.9.7--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for afterqc"
config: {"url": "https://biocontainers.pro/tools/afterqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for afterqc", "latest": {"0.9.7--hdfd78af_4": "sha256:5b4c109c25ac7808e9506097993854ba7fd06c542466b3606eb566452e91cb60"}, "tags": {"0.9.7--hdfd78af_4": "sha256:5b4c109c25ac7808e9506097993854ba7fd06c542466b3606eb566452e91cb60"}, "docker": "quay.io/biocontainers/afterqc", "aliases": {"after.py": "/usr/local/bin/after.py", "barcodeprocesser.py": "/usr/local/bin/barcodeprocesser.py", "bubbledetector.py": "/usr/local/bin/bubbledetector.py", "bubbleprocesser.py": "/usr/local/bin/bubbleprocesser.py", "circledetector.py": "/usr/local/bin/circledetector.py", "debubble.py": "/usr/local/bin/debubble.py", "fastq.py": "/usr/local/bin/fastq.py", "preprocesser.py": "/usr/local/bin/preprocesser.py", "qcreporter.py": "/usr/local/bin/qcreporter.py", "qualitycontrol.py": "/usr/local/bin/qualitycontrol.py", "util.py": "/usr/local/bin/util.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/afterqc.
shpc-registry automated BioContainers addition for afterqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/afterqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/afterqc:0.9.7--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/afterqc/0.9.7--hdfd78af_4
$ module help quay.io/biocontainers/afterqc/0.9.7--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### afterqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### afterqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### afterqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### afterqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### afterqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### afterqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### after.py

```bash
$ singularity exec <container> /usr/local/bin/after.py
$ podman run --it --rm --entrypoint /usr/local/bin/after.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/after.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barcodeprocesser.py

```bash
$ singularity exec <container> /usr/local/bin/barcodeprocesser.py
$ podman run --it --rm --entrypoint /usr/local/bin/barcodeprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barcodeprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bubbledetector.py

```bash
$ singularity exec <container> /usr/local/bin/bubbledetector.py
$ podman run --it --rm --entrypoint /usr/local/bin/bubbledetector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bubbledetector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bubbleprocesser.py

```bash
$ singularity exec <container> /usr/local/bin/bubbleprocesser.py
$ podman run --it --rm --entrypoint /usr/local/bin/bubbleprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bubbleprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circledetector.py

```bash
$ singularity exec <container> /usr/local/bin/circledetector.py
$ podman run --it --rm --entrypoint /usr/local/bin/circledetector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circledetector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debubble.py

```bash
$ singularity exec <container> /usr/local/bin/debubble.py
$ podman run --it --rm --entrypoint /usr/local/bin/debubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq.py

```bash
$ singularity exec <container> /usr/local/bin/fastq.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocesser.py

```bash
$ singularity exec <container> /usr/local/bin/preprocesser.py
$ podman run --it --rm --entrypoint /usr/local/bin/preprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocesser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcreporter.py

```bash
$ singularity exec <container> /usr/local/bin/qcreporter.py
$ podman run --it --rm --entrypoint /usr/local/bin/qcreporter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcreporter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualitycontrol.py

```bash
$ singularity exec <container> /usr/local/bin/qualitycontrol.py
$ podman run --it --rm --entrypoint /usr/local/bin/qualitycontrol.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualitycontrol.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### util.py

```bash
$ singularity exec <container> /usr/local/bin/util.py
$ podman run --it --rm --entrypoint /usr/local/bin/util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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