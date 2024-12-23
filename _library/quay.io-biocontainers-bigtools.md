---
layout: container
name:  "quay.io/biocontainers/bigtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bigtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bigtools/container.yaml"
updated_at: "2024-12-23 03:12:32.261822"
latest: "0.5.4--h715e4b3_0"
container_url: "https://biocontainers.pro/tools/bigtools"
aliases:
 - "bedgraphtobigwig"
 - "bedtobigbed"
 - "bigbedinfo"
 - "bigbedtobed"
 - "bigtools"
 - "bigwigaverageoverbed"
 - "bigwiginfo"
 - "bigwigmerge"
 - "bigwigtobedgraph"
 - "bigwigvaluesoverbed"
versions:
 - "0.4.1--h031d066_0"
 - "0.4.2--h031d066_0"
 - "0.4.3--h715e4b3_0"
 - "0.5.1--h715e4b3_0"
 - "0.5.2--h715e4b3_0"
 - "0.5.3--h715e4b3_0"
 - "0.5.4--h715e4b3_0"
description: "singularity registry hpc automated addition for bigtools"
config: {"url": "https://biocontainers.pro/tools/bigtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bigtools", "latest": {"0.5.4--h715e4b3_0": "sha256:335c686bdf72e0cf412fbfe37ea2f6dd72003c95ca8c9f1bae0e07319c4ec793"}, "tags": {"0.4.1--h031d066_0": "sha256:64fba24fad37fd4d53321adddf46ec21a2de4028ecceb4f099f5434218f836f9", "0.4.2--h031d066_0": "sha256:84001d75d09d8b275336847bd1a57eb2b820f068e7c2fb40fdce30cddf1116e9", "0.4.3--h715e4b3_0": "sha256:b0694cd0b518efa0af32d43f74b02291fd9d29f896cec38da934a30b264d4df1", "0.5.1--h715e4b3_0": "sha256:61e1a0826b1aaa1f76d76a308b28f6871cf487665bd63a63d8486be26dd4724b", "0.5.2--h715e4b3_0": "sha256:ee9573c8ddf2a9cc2beb3cc2fe75e964279dca31f8a2eeed7df2f2c79a1ef742", "0.5.3--h715e4b3_0": "sha256:ae720b65632c7c7e4e6f6bd67bfdc39ad338efcbeda0bab51072e99d531dba3a", "0.5.4--h715e4b3_0": "sha256:335c686bdf72e0cf412fbfe37ea2f6dd72003c95ca8c9f1bae0e07319c4ec793"}, "docker": "quay.io/biocontainers/bigtools", "aliases": {"bedgraphtobigwig": "/usr/local/bin/bedgraphtobigwig", "bedtobigbed": "/usr/local/bin/bedtobigbed", "bigbedinfo": "/usr/local/bin/bigbedinfo", "bigbedtobed": "/usr/local/bin/bigbedtobed", "bigtools": "/usr/local/bin/bigtools", "bigwigaverageoverbed": "/usr/local/bin/bigwigaverageoverbed", "bigwiginfo": "/usr/local/bin/bigwiginfo", "bigwigmerge": "/usr/local/bin/bigwigmerge", "bigwigtobedgraph": "/usr/local/bin/bigwigtobedgraph", "bigwigvaluesoverbed": "/usr/local/bin/bigwigvaluesoverbed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bigtools.
singularity registry hpc automated addition for bigtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bigtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bigtools:0.5.4--h715e4b3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bigtools/0.5.4--h715e4b3_0
$ module help quay.io/biocontainers/bigtools/0.5.4--h715e4b3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bigtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bigtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bigtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bigtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bigtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bigtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedgraphtobigwig

```bash
$ singularity exec <container> /usr/local/bin/bedgraphtobigwig
$ podman run --it --rm --entrypoint /usr/local/bin/bedgraphtobigwig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedgraphtobigwig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtobigbed

```bash
$ singularity exec <container> /usr/local/bin/bedtobigbed
$ podman run --it --rm --entrypoint /usr/local/bin/bedtobigbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtobigbed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigbedinfo

```bash
$ singularity exec <container> /usr/local/bin/bigbedinfo
$ podman run --it --rm --entrypoint /usr/local/bin/bigbedinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigbedinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigbedtobed

```bash
$ singularity exec <container> /usr/local/bin/bigbedtobed
$ podman run --it --rm --entrypoint /usr/local/bin/bigbedtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigbedtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigtools

```bash
$ singularity exec <container> /usr/local/bin/bigtools
$ podman run --it --rm --entrypoint /usr/local/bin/bigtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigaverageoverbed

```bash
$ singularity exec <container> /usr/local/bin/bigwigaverageoverbed
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigaverageoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigaverageoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwiginfo

```bash
$ singularity exec <container> /usr/local/bin/bigwiginfo
$ podman run --it --rm --entrypoint /usr/local/bin/bigwiginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwiginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigmerge

```bash
$ singularity exec <container> /usr/local/bin/bigwigmerge
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigtobedgraph

```bash
$ singularity exec <container> /usr/local/bin/bigwigtobedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigtobedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigtobedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigvaluesoverbed

```bash
$ singularity exec <container> /usr/local/bin/bigwigvaluesoverbed
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigvaluesoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigvaluesoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
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