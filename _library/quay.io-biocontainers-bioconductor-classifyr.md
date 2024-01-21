---
layout: container
name:  "quay.io/biocontainers/bioconductor-classifyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-classifyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-classifyr/container.yaml"
updated_at: "2024-01-21 02:36:43.956765"
latest: "3.6.2--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-classifyr"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r40_0"
 - "3.2.0--r42hc247a5b_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r40hdfd78af_1"
 - "3.2.0--r42hf17093f_1"
 - "3.4.7--r43hf17093f_1"
 - "3.6.2--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-classifyr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-classifyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-classifyr", "latest": {"3.6.2--r43hf17093f_0": "sha256:dc48aaa906a25de89abacdbf426d3c3b1736ecfa2be3d5d9952c39d36976f617"}, "tags": {"2.8.0--r40_0": "sha256:f14cdb92ef54f296956a34c84ff3b51c062697fce76667c9a0108c67999c134c", "3.2.0--r42hc247a5b_0": "sha256:81f599d5e2347abf65ad52754a8f6ca49cdf7e701d50f4c67405d91681382851", "2.14.0--r41hdfd78af_0": "sha256:238595df9192fe5729da0d54f75a8ff7bf9ca4d851c02af6d45695fac02254e7", "2.12.0--r41hdfd78af_0": "sha256:c7f088f2602a1167123519801ab310f617bafb7cdf559bc60b200b95f2af6fe4", "2.10.0--r40hdfd78af_1": "sha256:8800a5846723f03513543cf7f7233b25fa9f90ae12a2538e7f188096fa69fc8d", "3.2.0--r42hf17093f_1": "sha256:9da8ca4d497f82261a1ea09dd4f5e547a5b7f1e87319df475037f5188ec04c30", "3.4.7--r43hf17093f_1": "sha256:1075758b7168fbe9dae1c638c7ad848124a00d68327d6540d43e4916698439a2", "3.6.2--r43hf17093f_0": "sha256:dc48aaa906a25de89abacdbf426d3c3b1736ecfa2be3d5d9952c39d36976f617"}, "docker": "quay.io/biocontainers/bioconductor-classifyr", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-classifyr.
shpc-registry automated BioContainers addition for bioconductor-classifyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-classifyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-classifyr:3.6.2--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-classifyr/3.6.2--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-classifyr/3.6.2--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-classifyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-classifyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-classifyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-classifyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-classifyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-classifyr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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