---
layout: container
name:  "quay.io/biocontainers/primedlamp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primedlamp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primedlamp/container.yaml"
updated_at: "2025-05-11 03:51:47.872455"
latest: "1.0.1--py_0"
container_url: "https://biocontainers.pro/tools/primedlamp"
aliases:
 - "PrimedLAMP"
 - "PrimedLAMP_Amplicon_Success"
 - "PrimedLAMP_Cross_Reactivity_Update"
 - "PrimedLAMP_Custom"
 - "PrimedLAMP_Inclusivity_Update"
 - "PrimedLAMP_Tm_Update"
 - "clustalo"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
 - "bt-context.txt"
 - "bt-link"
versions:
 - "1.0.1--py_0"
description: "shpc-registry automated BioContainers addition for primedlamp"
config: {"url": "https://biocontainers.pro/tools/primedlamp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primedlamp", "latest": {"1.0.1--py_0": "sha256:5f9c38a1d98d15e707bfdb54ff4c66ec04d16c62dbd1a7a599378cd20bce19e1"}, "tags": {"1.0.1--py_0": "sha256:5f9c38a1d98d15e707bfdb54ff4c66ec04d16c62dbd1a7a599378cd20bce19e1"}, "docker": "quay.io/biocontainers/primedlamp", "aliases": {"PrimedLAMP": "/usr/local/bin/PrimedLAMP", "PrimedLAMP_Amplicon_Success": "/usr/local/bin/PrimedLAMP_Amplicon_Success", "PrimedLAMP_Cross_Reactivity_Update": "/usr/local/bin/PrimedLAMP_Cross_Reactivity_Update", "PrimedLAMP_Custom": "/usr/local/bin/PrimedLAMP_Custom", "PrimedLAMP_Inclusivity_Update": "/usr/local/bin/PrimedLAMP_Inclusivity_Update", "PrimedLAMP_Tm_Update": "/usr/local/bin/PrimedLAMP_Tm_Update", "clustalo": "/usr/local/bin/clustalo", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf", "bt-context.txt": "/usr/local/bin/bt-context.txt", "bt-link": "/usr/local/bin/bt-link"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primedlamp.
shpc-registry automated BioContainers addition for primedlamp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primedlamp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primedlamp:1.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primedlamp/1.0.1--py_0
$ module help quay.io/biocontainers/primedlamp/1.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primedlamp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primedlamp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primedlamp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primedlamp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primedlamp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primedlamp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PrimedLAMP

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrimedLAMP_Amplicon_Success

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP_Amplicon_Success
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Amplicon_Success   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Amplicon_Success   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrimedLAMP_Cross_Reactivity_Update

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP_Cross_Reactivity_Update
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Cross_Reactivity_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Cross_Reactivity_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrimedLAMP_Custom

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP_Custom
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Custom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Custom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrimedLAMP_Inclusivity_Update

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP_Inclusivity_Update
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Inclusivity_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Inclusivity_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrimedLAMP_Tm_Update

```bash
$ singularity exec <container> /usr/local/bin/PrimedLAMP_Tm_Update
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Tm_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedLAMP_Tm_Update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-context.txt

```bash
$ singularity exec <container> /usr/local/bin/bt-context.txt
$ podman run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-link

```bash
$ singularity exec <container> /usr/local/bin/bt-link
$ podman run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
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