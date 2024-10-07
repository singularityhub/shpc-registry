---
layout: container
name:  "quay.io/biocontainers/bioconductor-mapscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mapscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mapscape/container.yaml"
updated_at: "2024-10-07 16:26:45.891280"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mapscape"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r361_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mapscape"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mapscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mapscape", "latest": {"1.26.0--r43hdfd78af_0": "sha256:1ea6b6253064398e6dbe4b2a6c6a438065fc034520b84d3e8d1b82bd4bbef6f3"}, "tags": {"1.8.0--r361_1": "sha256:b2b784f910e90d344f520702f6e61e2a1142df3b1a79726c302cd25b27a2f36e", "1.18.0--r41hdfd78af_0": "sha256:842eff0a43d02d91bcf8c6c87a315b454a586b73f688b1b45bd6763879fb79c0", "1.16.0--r41hdfd78af_0": "sha256:aae97da97d4bea343e6cde9abe48da9c9238375c5324769a2d1b2530840bc069", "1.14.0--r40hdfd78af_1": "sha256:fe30d6a0e75c95f5acb29692e69a003383ed4b6e8169fad0c9e0beeca69a8223", "1.12.0--r40_0": "sha256:3389570772d177d3bcd83e9185679b04069b554042b6d6790d1d2a5eed79ff07", "1.10.0--r36_0": "sha256:c494bd842465e874b21d734ebce98bced759ed20b296b13bdb7ea44eb6f73c2a", "1.22.0--r42hdfd78af_0": "sha256:aea5ae81218d7318c6f04cef93a1555dfdca0175cc0a63e2147a337b18ea1d27", "1.24.0--r43hdfd78af_0": "sha256:ca248d545f949058165c42fe53775af6a343c77d272aea123a1160bceaa8ca3f", "1.26.0--r43hdfd78af_0": "sha256:1ea6b6253064398e6dbe4b2a6c6a438065fc034520b84d3e8d1b82bd4bbef6f3"}, "docker": "quay.io/biocontainers/bioconductor-mapscape", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mapscape.
shpc-registry automated BioContainers addition for bioconductor-mapscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mapscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mapscape:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mapscape/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mapscape/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mapscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mapscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mapscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mapscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
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