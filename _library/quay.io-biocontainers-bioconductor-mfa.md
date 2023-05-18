---
layout: container
name:  "quay.io/biocontainers/bioconductor-mfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mfa/container.yaml"
updated_at: "2023-05-18 02:44:08.251077"
latest: "1.20.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mfa"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41h399db7b_0"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mfa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mfa", "latest": {"1.20.0--r42hc247a5b_0": "sha256:121424609bc5721cbe05c53ac1f9aee9996010a2291ff6ca147518c9679576bc"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:de69067bce4482a27ba77eaa19f1ab6a4be9cc7370083e2fc8675063753bed26", "1.20.0--r42hc247a5b_0": "sha256:121424609bc5721cbe05c53ac1f9aee9996010a2291ff6ca147518c9679576bc", "1.16.0--r41h399db7b_0": "sha256:acfb6384176d1272b2088871f08ffacdb24b8cf80da750f174ef05fcb9ab4059", "1.14.0--r41h399db7b_0": "sha256:5dd6a951b73e6997cbd8fd97ed2df8717a9ce132f586f224e1046ac0ba72f0c6", "1.12.0--r40h399db7b_1": "sha256:d4dc67f23fc558f0ae60c63e835dd97c3199ffb8f963c2c559288c76262a6ea4", "1.10.0--r40h5f743cb_0": "sha256:78caf21524b615113510d70162fcb60d745c5a4971e45ed468c41e0715b412d0"}, "docker": "quay.io/biocontainers/bioconductor-mfa", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mfa.
shpc-registry automated BioContainers addition for bioconductor-mfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mfa:1.20.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mfa/1.20.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-mfa/1.20.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mfa-inspect-deffile:

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