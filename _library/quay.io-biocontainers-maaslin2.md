---
layout: container
name:  "quay.io/biocontainers/maaslin2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maaslin2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maaslin2/container.yaml"
updated_at: "2023-10-23 02:45:12.933880"
latest: "0.99.12--r36_0"
container_url: "https://biocontainers.pro/tools/maaslin2"
aliases:
 - "Maaslin2.R"
 - "fit.R"
 - "utility_scripts.R"
 - "viz.R"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "0.99.2--r351_0"
 - "0.99.12--r36_0"
description: "shpc-registry automated BioContainers addition for maaslin2"
config: {"url": "https://biocontainers.pro/tools/maaslin2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for maaslin2", "latest": {"0.99.12--r36_0": "sha256:6ada70bef34426a3f6ee241b17af26d5e5c6002a29495a82b7bdd49e1e6beb6d"}, "tags": {"0.99.2--r351_0": "sha256:8f49f38247c928b5eb175fe3266da05f729d5c26f5e48fbd894110e8858546e3", "0.99.12--r36_0": "sha256:6ada70bef34426a3f6ee241b17af26d5e5c6002a29495a82b7bdd49e1e6beb6d"}, "docker": "quay.io/biocontainers/maaslin2", "aliases": {"Maaslin2.R": "/usr/local/bin/Maaslin2.R", "fit.R": "/usr/local/bin/fit.R", "utility_scripts.R": "/usr/local/bin/utility_scripts.R", "viz.R": "/usr/local/bin/viz.R", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maaslin2.
shpc-registry automated BioContainers addition for maaslin2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maaslin2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maaslin2:0.99.12--r36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maaslin2/0.99.12--r36_0
$ module help quay.io/biocontainers/maaslin2/0.99.12--r36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maaslin2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maaslin2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maaslin2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maaslin2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maaslin2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maaslin2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Maaslin2.R

```bash
$ singularity exec <container> /usr/local/bin/Maaslin2.R
$ podman run --it --rm --entrypoint /usr/local/bin/Maaslin2.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Maaslin2.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fit.R

```bash
$ singularity exec <container> /usr/local/bin/fit.R
$ podman run --it --rm --entrypoint /usr/local/bin/fit.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fit.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utility_scripts.R

```bash
$ singularity exec <container> /usr/local/bin/utility_scripts.R
$ podman run --it --rm --entrypoint /usr/local/bin/utility_scripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utility_scripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viz.R

```bash
$ singularity exec <container> /usr/local/bin/viz.R
$ podman run --it --rm --entrypoint /usr/local/bin/viz.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viz.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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