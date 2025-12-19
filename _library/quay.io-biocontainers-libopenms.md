---
layout: container
name:  "quay.io/biocontainers/libopenms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libopenms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libopenms/container.yaml"
updated_at: "2025-12-19 05:38:50.874525"
latest: "3.4.1--hdd6e20e_1"
container_url: "https://biocontainers.pro/tools/libopenms"
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
 - "2.8.0--h7ca0330_3"
 - "2.8.0--h604f271_4"
 - "2.9.1--h135471a_0"
 - "2.9.1--h135471a_1"
 - "2.9.1--h8964181_4"
 - "3.0.0--h8964181_1"
 - "3.1.0--h8964181_3"
 - "3.1.0--h191ead1_4"
 - "3.2.0--haddbca4_4"
 - "3.2.0--haddbca4_5"
 - "3.3.0--h0656172_6"
 - "3.3.0--h0656172_8"
 - "3.4.0--hc77a4c7_0"
 - "3.4.1--heb594b5_0"
 - "3.4.1--hdd6e20e_1"
description: "shpc-registry automated BioContainers addition for libopenms"
config: {"url": "https://biocontainers.pro/tools/libopenms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libopenms", "latest": {"3.4.1--hdd6e20e_1": "sha256:d5cd2d90efe58bf3779546cc26a8604b20bc051bcf7ba487f7d4af462833a2b1"}, "tags": {"2.8.0--h7ca0330_3": "sha256:a33b2779973c820f1a2c311949f9c8b3cbb6196fa8ac4a0b4e3bdaf90833d729", "2.8.0--h604f271_4": "sha256:a7da8fd8b63bf4d8f0aaf5b609d2c3a285fc97fefd01f879e7931a610a83cea7", "2.9.1--h135471a_0": "sha256:f520e3ce43d6a15161036916404e61679a071f069cc26f1ae07659399e999998", "2.9.1--h135471a_1": "sha256:644dc021ad8ab6bce782d1c9bec50c3a48917a82f3c6baab3ea422b12e1345f1", "2.9.1--h8964181_4": "sha256:3346d2a757ed0ea79bc020161850a79f3394ee7529c873ca70338ac41d8fe742", "3.0.0--h8964181_1": "sha256:0e48e688cbb8ae9455c9f59c7bd146bf8e08754088f05c949ccad5ca44ac76e7", "3.1.0--h8964181_3": "sha256:5b0c14189816d83a20dcb7817bf2a1019aa7dadda929e043af9a77d155a5cc87", "3.1.0--h191ead1_4": "sha256:96fe6e34e8472fadb2185663498913a123d632c677072684c68069fa87942941", "3.2.0--haddbca4_4": "sha256:786ced82a0cced6dc38ce557612831ce8b8da62bd2ec8530c78627bc6405d928", "3.2.0--haddbca4_5": "sha256:e796acf38a8c3b902fbc2b3160c5dfbbb78e31537d3834a500ad30f8de2848d5", "3.3.0--h0656172_6": "sha256:aee2ce23df8e9c40c73936b614a72ec7a00bb4743bd373c54ba4bc7247277c52", "3.3.0--h0656172_8": "sha256:f871f3b809721acb5dcafc4564604dc55f0caea9670b83680605c79c866c5261", "3.4.0--hc77a4c7_0": "sha256:8b08e413a7f68b9086c6f3aab75fca1ba941a50d0af623eccf3c1f8bf0730201", "3.4.1--heb594b5_0": "sha256:454b05610f964a270e9309f100dbfa7be15cc5ca0079ebc3eb4facfb71dd2490", "3.4.1--hdd6e20e_1": "sha256:d5cd2d90efe58bf3779546cc26a8604b20bc051bcf7ba487f7d4af462833a2b1"}, "docker": "quay.io/biocontainers/libopenms", "aliases": {"CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter", "Redirect": "/usr/local/bin/Redirect", "SAX2Count": "/usr/local/bin/SAX2Count", "SAX2Print": "/usr/local/bin/SAX2Print"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libopenms.
shpc-registry automated BioContainers addition for libopenms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libopenms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libopenms:3.4.1--hdd6e20e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libopenms/3.4.1--hdd6e20e_1
$ module help quay.io/biocontainers/libopenms/3.4.1--hdd6e20e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libopenms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libopenms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libopenms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libopenms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libopenms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libopenms-inspect-deffile:

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