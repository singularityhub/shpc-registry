---
layout: container
name:  "quay.io/biocontainers/hmftools-amber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-amber/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-amber/container.yaml"
updated_at: "2025-12-28 04:09:14.964255"
latest: "4.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-amber"
aliases:
 - "AMBER"
 - "jpackage"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jfr"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
versions:
 - "3.9--hdfd78af_1"
 - "4.0--hdfd78af_0"
 - "3.9.1--hdfd78af_0"
 - "4.0.1--hdfd78af_0"
 - "4.1_beta--hdfd78af_0"
 - "4.1_beta--hdfd78af_1"
 - "4.1.1--hdfd78af_0"
 - "4.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-amber"
config: {"url": "https://biocontainers.pro/tools/hmftools-amber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-amber", "latest": {"4.2--hdfd78af_0": "sha256:16741972ca9fc2e6ee8f2456e2b629479f38c898cc307df68efec0c5f4af2d9b"}, "tags": {"3.9--hdfd78af_1": "sha256:2735782fa475aed6f552b466dcd7ca4f03e7431e4555f1369d67d088b04d0247", "4.0--hdfd78af_0": "sha256:4bead7f67388476a14b043d86fdc9b0636e532a9329d418a1b438cea23e3bb74", "3.9.1--hdfd78af_0": "sha256:37c09c6d4eeebc11824ecf08a75ab17e9197176b54f4a731259f0708b9c8530c", "4.0.1--hdfd78af_0": "sha256:8060c8e9da99a1fa518ac6d32f3026a589c3d3e737c2c2ca025e963a8dea1818", "4.1_beta--hdfd78af_0": "sha256:af9b68c982155931c518f3df41ed761287b045a2341ad1d5a8d40c2be53cef41", "4.1_beta--hdfd78af_1": "sha256:dd2c085535e2d0793f7fe36974d85babb7c6ea1f206efd5a99e92f20cb1745a5", "4.1.1--hdfd78af_0": "sha256:780604a4fd0e2933852f093b570d159f06a390567069ea1fd22420723a57d340", "4.2--hdfd78af_0": "sha256:16741972ca9fc2e6ee8f2456e2b629479f38c898cc307df68efec0c5f4af2d9b"}, "docker": "quay.io/biocontainers/hmftools-amber", "aliases": {"AMBER": "/usr/local/bin/AMBER", "jpackage": "/usr/local/bin/jpackage", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jfr": "/usr/local/bin/jfr", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-amber.
shpc-registry automated BioContainers addition for hmftools-amber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-amber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-amber:4.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-amber/4.2--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-amber/4.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-amber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-amber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-amber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-amber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-amber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-amber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMBER

```bash
$ singularity exec <container> /usr/local/bin/AMBER
$ podman run --it --rm --entrypoint /usr/local/bin/AMBER   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMBER   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
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