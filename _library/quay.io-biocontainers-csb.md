---
layout: container
name:  "quay.io/biocontainers/csb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/csb/container.yaml"
updated_at: "2024-01-01 03:19:22.100037"
latest: "1.2.5--pyh24bf2e0_2"
container_url: "https://biocontainers.pro/tools/csb"
aliases:
 - "csb-bfit"
 - "csb-bfite"
 - "csb-buildhmm"
 - "csb-csfrag"
 - "csb-embd"
 - "csb-hhfrag"
 - "csb-hhsearch"
 - "csb-precision"
 - "csb-promix"
 - "csb-test"
 - "qhelpconverter"
 - "pylupdate5"
 - "pyrcc5"
 - "pyuic5"
 - "sip"
 - "qdoc"
 - "gst-device-monitor-1.0"
 - "gst-discoverer-1.0"
 - "gst-play-1.0"
 - "fixqt4headers.pl"
versions:
 - "1.2.5--pyh24bf2e0_2"
description: "shpc-registry automated BioContainers addition for csb"
config: {"url": "https://biocontainers.pro/tools/csb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for csb", "latest": {"1.2.5--pyh24bf2e0_2": "sha256:78eb0352517ed26a0055570aa2e1f900b7086084b42e92b13ad76c2774101f5e"}, "tags": {"1.2.5--pyh24bf2e0_2": "sha256:78eb0352517ed26a0055570aa2e1f900b7086084b42e92b13ad76c2774101f5e"}, "docker": "quay.io/biocontainers/csb", "aliases": {"csb-bfit": "/usr/local/bin/csb-bfit", "csb-bfite": "/usr/local/bin/csb-bfite", "csb-buildhmm": "/usr/local/bin/csb-buildhmm", "csb-csfrag": "/usr/local/bin/csb-csfrag", "csb-embd": "/usr/local/bin/csb-embd", "csb-hhfrag": "/usr/local/bin/csb-hhfrag", "csb-hhsearch": "/usr/local/bin/csb-hhsearch", "csb-precision": "/usr/local/bin/csb-precision", "csb-promix": "/usr/local/bin/csb-promix", "csb-test": "/usr/local/bin/csb-test", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5", "pyuic5": "/usr/local/bin/pyuic5", "sip": "/usr/local/bin/sip", "qdoc": "/usr/local/bin/qdoc", "gst-device-monitor-1.0": "/usr/local/bin/gst-device-monitor-1.0", "gst-discoverer-1.0": "/usr/local/bin/gst-discoverer-1.0", "gst-play-1.0": "/usr/local/bin/gst-play-1.0", "fixqt4headers.pl": "/usr/local/bin/fixqt4headers.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csb.
shpc-registry automated BioContainers addition for csb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csb:1.2.5--pyh24bf2e0_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csb/1.2.5--pyh24bf2e0_2
$ module help quay.io/biocontainers/csb/1.2.5--pyh24bf2e0_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csb-bfit

```bash
$ singularity exec <container> /usr/local/bin/csb-bfit
$ podman run --it --rm --entrypoint /usr/local/bin/csb-bfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-bfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-bfite

```bash
$ singularity exec <container> /usr/local/bin/csb-bfite
$ podman run --it --rm --entrypoint /usr/local/bin/csb-bfite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-bfite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-buildhmm

```bash
$ singularity exec <container> /usr/local/bin/csb-buildhmm
$ podman run --it --rm --entrypoint /usr/local/bin/csb-buildhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-buildhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-csfrag

```bash
$ singularity exec <container> /usr/local/bin/csb-csfrag
$ podman run --it --rm --entrypoint /usr/local/bin/csb-csfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-csfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-embd

```bash
$ singularity exec <container> /usr/local/bin/csb-embd
$ podman run --it --rm --entrypoint /usr/local/bin/csb-embd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-embd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-hhfrag

```bash
$ singularity exec <container> /usr/local/bin/csb-hhfrag
$ podman run --it --rm --entrypoint /usr/local/bin/csb-hhfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-hhfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-hhsearch

```bash
$ singularity exec <container> /usr/local/bin/csb-hhsearch
$ podman run --it --rm --entrypoint /usr/local/bin/csb-hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-precision

```bash
$ singularity exec <container> /usr/local/bin/csb-precision
$ podman run --it --rm --entrypoint /usr/local/bin/csb-precision   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-precision   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-promix

```bash
$ singularity exec <container> /usr/local/bin/csb-promix
$ podman run --it --rm --entrypoint /usr/local/bin/csb-promix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-promix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-test

```bash
$ singularity exec <container> /usr/local/bin/csb-test
$ podman run --it --rm --entrypoint /usr/local/bin/csb-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylupdate5

```bash
$ singularity exec <container> /usr/local/bin/pylupdate5
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc5

```bash
$ singularity exec <container> /usr/local/bin/pyrcc5
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyuic5

```bash
$ singularity exec <container> /usr/local/bin/pyuic5
$ podman run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc

```bash
$ singularity exec <container> /usr/local/bin/qdoc
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-device-monitor-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-device-monitor-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-discoverer-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-discoverer-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-play-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-play-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixqt4headers.pl

```bash
$ singularity exec <container> /usr/local/bin/fixqt4headers.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fixqt4headers.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixqt4headers.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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