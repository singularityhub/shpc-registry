---
layout: container
name:  "quay.io/biocontainers/paml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paml/container.yaml"
updated_at: "2023-07-02 03:33:30.122054"
latest: "4.10.6--h031d066_2"
container_url: "https://biocontainers.pro/tools/paml"
aliases:
 - "baseml"
 - "basemlg"
 - "chi2"
 - "codeml"
 - "evolver"
 - "infinitesites"
 - "mcmctree"
 - "pamp"
 - "yn00"
versions:
 - "4.9--hec16e2b_7"
 - "4.10.6--hec16e2b_0"
 - "4.10.6--h031d066_2"
description: "shpc-registry automated BioContainers addition for paml"
config: {"url": "https://biocontainers.pro/tools/paml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for paml", "latest": {"4.10.6--h031d066_2": "sha256:5bc7ceea0bf33bc1975bffeb64e9c4ca3955fac9320d87dc5a443b405ac12cff"}, "tags": {"4.9--hec16e2b_7": "sha256:8a4612423d8664ba34989e4e085b7cd0ea9f9b730bac67d97bf61745768d5020", "4.10.6--hec16e2b_0": "sha256:c8d7a4fea26864f55e90300c84dfd0f8b61dd832e7e0a42e315d055285a3bc0e", "4.10.6--h031d066_2": "sha256:5bc7ceea0bf33bc1975bffeb64e9c4ca3955fac9320d87dc5a443b405ac12cff"}, "docker": "quay.io/biocontainers/paml", "aliases": {"baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "chi2": "/usr/local/bin/chi2", "codeml": "/usr/local/bin/codeml", "evolver": "/usr/local/bin/evolver", "infinitesites": "/usr/local/bin/infinitesites", "mcmctree": "/usr/local/bin/mcmctree", "pamp": "/usr/local/bin/pamp", "yn00": "/usr/local/bin/yn00"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paml.
shpc-registry automated BioContainers addition for paml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paml:4.10.6--h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paml/4.10.6--h031d066_2
$ module help quay.io/biocontainers/paml/4.10.6--h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chi2

```bash
$ singularity exec <container> /usr/local/bin/chi2
$ podman run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codeml

```bash
$ singularity exec <container> /usr/local/bin/codeml
$ podman run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolver

```bash
$ singularity exec <container> /usr/local/bin/evolver
$ podman run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infinitesites

```bash
$ singularity exec <container> /usr/local/bin/infinitesites
$ podman run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcmctree

```bash
$ singularity exec <container> /usr/local/bin/mcmctree
$ podman run --it --rm --entrypoint /usr/local/bin/mcmctree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcmctree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pamp

```bash
$ singularity exec <container> /usr/local/bin/pamp
$ podman run --it --rm --entrypoint /usr/local/bin/pamp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pamp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yn00

```bash
$ singularity exec <container> /usr/local/bin/yn00
$ podman run --it --rm --entrypoint /usr/local/bin/yn00   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yn00   -v ${PWD} -w ${PWD} <container> -c " $@"
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