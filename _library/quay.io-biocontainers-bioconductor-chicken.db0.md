---
layout: container
name:  "quay.io/biocontainers/bioconductor-chicken.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chicken.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chicken.db0/container.yaml"
updated_at: "2024-02-09 03:21:24.671809"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chicken.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chicken.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chicken.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chicken.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:ba4fdc34625f14a9732ecffeb11e3f717bc24de778a2de53b14a580a58c75aae"}, "tags": {"3.8.2--r36_1": "sha256:24aa5dba02d7f4df26e717bbadbae751d309a2f3a1b52f93f80b01018a900fdc", "3.16.0--r42hdfd78af_0": "sha256:23dee022de2fc643355e3206d17421e541b492005929d43d200837dd7a99add5", "3.14.0--r41hdfd78af_1": "sha256:373e42202c5c88b12313fca85bfcc567db8e5823d037dcc1c0a7fa3f1354ef47", "3.13.0--r41hdfd78af_0": "sha256:a729c42345dcc2a32c9e7f49e5678a80ccebc6b2a75fe50e51b87353ad641949", "3.12.0--r40hdfd78af_1": "sha256:afffe0f63b4f8bbe627525cf08a7cf0b4f560376190aafc97ed6238229abe10a", "3.11.2--r40_0": "sha256:72c4616dc485ce1d8285bca208b25b4b56d7a726150d4558cd205dfb7b5c73dc", "3.17.0--r43hdfd78af_0": "sha256:1da5bd421a02a3db51e2cf2287147f246beb4440fd3a9ffb7d75544d304f10f6", "3.18.0--r43hdfd78af_0": "sha256:ba4fdc34625f14a9732ecffeb11e3f717bc24de778a2de53b14a580a58c75aae"}, "docker": "quay.io/biocontainers/bioconductor-chicken.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chicken.db0.
shpc-registry automated BioContainers addition for bioconductor-chicken.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chicken.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chicken.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chicken.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chicken.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chicken.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicken.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicken.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chicken.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chicken.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chicken.db0-inspect-deffile:

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