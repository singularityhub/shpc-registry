---
layout: container
name:  "quay.io/biocontainers/r-monocle3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-monocle3/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-monocle3/container.yaml"
updated_at: "2022-10-29 05:56:56.536652"
latest: "1.0.0--r41h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/r-monocle3"
aliases:
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
 - "Redirect"
 - "SAX2Count"
 - "SAX2Print"
versions:
 - "1.0.0--r41h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for r-monocle3"
config: {"url": "https://biocontainers.pro/tools/r-monocle3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-monocle3", "latest": {"1.0.0--r41h9f5acd7_2": "sha256:d4852b89fa06b6f62f4abd30679cc92368e8c49beea05a1ccaae664a3962152e"}, "tags": {"1.0.0--r41h9f5acd7_2": "sha256:d4852b89fa06b6f62f4abd30679cc92368e8c49beea05a1ccaae664a3962152e"}, "docker": "quay.io/biocontainers/r-monocle3", "aliases": {"CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter", "Redirect": "/usr/local/bin/Redirect", "SAX2Count": "/usr/local/bin/SAX2Count", "SAX2Print": "/usr/local/bin/SAX2Print"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-monocle3.
shpc-registry automated BioContainers addition for r-monocle3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-monocle3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-monocle3:1.0.0--r41h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-monocle3/1.0.0--r41h9f5acd7_2
$ module help quay.io/biocontainers/r-monocle3/1.0.0--r41h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-monocle3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-monocle3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-monocle3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-monocle3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-monocle3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-monocle3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect

```bash
$ singularity exec <container> /usr/local/bin/Redirect
$ podman run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count

```bash
$ singularity exec <container> /usr/local/bin/SAX2Count
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print

```bash
$ singularity exec <container> /usr/local/bin/SAX2Print
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
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