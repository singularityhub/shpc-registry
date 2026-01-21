---
layout: container
name:  "quay.io/biocontainers/consent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/consent/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/consent/container.yaml"
updated_at: "2026-01-21 04:30:51.152279"
latest: "2.2.2--h3452944_6"
container_url: "https://biocontainers.pro/tools/consent"
aliases:
 - "CONSENT-correct"
 - "CONSENT-correction"
 - "CONSENT-explode"
 - "CONSENT-merge"
 - "CONSENT-polish"
 - "CONSENT-polishing"
 - "CONSENT-reformatPAF"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
versions:
 - "2.2.2--h5b5514e_2"
 - "2.2.2--h5b5514e_3"
 - "2.2.2--hdb21b49_4"
 - "2.2.2--h3452944_6"
description: "shpc-registry automated BioContainers addition for consent"
config: {"url": "https://biocontainers.pro/tools/consent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for consent", "latest": {"2.2.2--h3452944_6": "sha256:2aa415fa07d50d79043915351dfd846a78404ec7b3a73dc4368306446effebed"}, "tags": {"2.2.2--h5b5514e_2": "sha256:98f032fc58c454aafcbf1b47edcc57ac35b7dca2f5ee08b91b253da292c43940", "2.2.2--h5b5514e_3": "sha256:e8aa2c4888e551e61964aa8e01f4056772c2cc93975e595e0ab87ede5bb8f75a", "2.2.2--hdb21b49_4": "sha256:488d44434201ff24fc96a31ab1406347479bf2db9e8fe6df1185b271a855fb43", "2.2.2--h3452944_6": "sha256:2aa415fa07d50d79043915351dfd846a78404ec7b3a73dc4368306446effebed"}, "docker": "quay.io/biocontainers/consent", "aliases": {"CONSENT-correct": "/usr/local/bin/CONSENT-correct", "CONSENT-correction": "/usr/local/bin/CONSENT-correction", "CONSENT-explode": "/usr/local/bin/CONSENT-explode", "CONSENT-merge": "/usr/local/bin/CONSENT-merge", "CONSENT-polish": "/usr/local/bin/CONSENT-polish", "CONSENT-polishing": "/usr/local/bin/CONSENT-polishing", "CONSENT-reformatPAF": "/usr/local/bin/CONSENT-reformatPAF", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/consent.
shpc-registry automated BioContainers addition for consent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/consent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/consent:2.2.2--h3452944_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/consent/2.2.2--h3452944_6
$ module help quay.io/biocontainers/consent/2.2.2--h3452944_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CONSENT-correct

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-correct
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-correction

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-correction
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-correction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-correction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-explode

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-explode
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-explode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-explode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-merge

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-merge
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-polish

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-polish
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-polish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-polish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-polishing

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-polishing
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-polishing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-polishing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CONSENT-reformatPAF

```bash
$ singularity exec <container> /usr/local/bin/CONSENT-reformatPAF
$ podman run --it --rm --entrypoint /usr/local/bin/CONSENT-reformatPAF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CONSENT-reformatPAF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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