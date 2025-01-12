---
layout: container
name:  "quay.io/biocontainers/clust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clust/container.yaml"
updated_at: "2025-01-12 03:27:24.842452"
latest: "1.18.0--pyh086e186_0"
container_url: "https://biocontainers.pro/tools/clust"
aliases:
 - "clust"
 - "conv-template"
 - "from-template"
 - "qhelpconverter"
 - "pylupdate5"
 - "pyrcc5"
 - "pyuic5"
 - "sip"
 - "qdoc"
 - "gst-device-monitor-1.0"
 - "gst-discoverer-1.0"
versions:
 - "1.8.9--py27h24bf2e0_0"
 - "1.17.0--pyhfa5458b_0"
 - "1.12.0--pyh145b6a8_0"
 - "1.10.12--pyh145b6a8_0"
 - "1.8.10--py27h24bf2e0_0"
 - "1.18.0--pyh086e186_0"
description: "shpc-registry automated BioContainers addition for clust"
config: {"url": "https://biocontainers.pro/tools/clust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clust", "latest": {"1.18.0--pyh086e186_0": "sha256:6ee79d7c6236cbbdae110b5db65f0ca2cb8f4174b1b30af6ac795fd1ab2427de"}, "tags": {"1.8.9--py27h24bf2e0_0": "sha256:7a225c4dac8c501e9b58f6f6c914ba21d6501cd430464189ca1df9be2faf6507", "1.17.0--pyhfa5458b_0": "sha256:82600f1b98749730ec19c120b9f27f55a8961779d912b3ff3fff8b4d4c760921", "1.12.0--pyh145b6a8_0": "sha256:8018bd8dc805f94054bc37e7a60086303d476a67c7438156e910f87b8be3d0df", "1.10.12--pyh145b6a8_0": "sha256:bf89164a103e1b344ac24c1c0586e8699147a4a97aee36001e82112b37011647", "1.8.10--py27h24bf2e0_0": "sha256:ede3e3fd0afa93a2f553d6158ad5d885f66524389673e82db0765c2517fb286b", "1.18.0--pyh086e186_0": "sha256:6ee79d7c6236cbbdae110b5db65f0ca2cb8f4174b1b30af6ac795fd1ab2427de"}, "docker": "quay.io/biocontainers/clust", "aliases": {"clust": "/usr/local/bin/clust", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5", "pyuic5": "/usr/local/bin/pyuic5", "sip": "/usr/local/bin/sip", "qdoc": "/usr/local/bin/qdoc", "gst-device-monitor-1.0": "/usr/local/bin/gst-device-monitor-1.0", "gst-discoverer-1.0": "/usr/local/bin/gst-discoverer-1.0"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clust.
shpc-registry automated BioContainers addition for clust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clust:1.18.0--pyh086e186_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clust/1.18.0--pyh086e186_0
$ module help quay.io/biocontainers/clust/1.18.0--pyh086e186_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clust

```bash
$ singularity exec <container> /usr/local/bin/clust
$ podman run --it --rm --entrypoint /usr/local/bin/clust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
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