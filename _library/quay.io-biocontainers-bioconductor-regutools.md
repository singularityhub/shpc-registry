---
layout: container
name:  "quay.io/biocontainers/bioconductor-regutools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-regutools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-regutools/container.yaml"
updated_at: "2024-04-06 02:33:00.351335"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-regutools"
aliases:
 - "Cytoscape"
 - "cytoscape.sh"
 - "gen_vmoptions.sh"
 - "curve_keygen"
 - "jaotc"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-regutools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-regutools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-regutools", "latest": {"1.14.0--r43hdfd78af_0": "sha256:b526c6242e4d977a9b2cbb43ba9cf9fd5e8fb2c0bb7bbf9f342073998cc9f6e1"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:3a5cee7cd010df6f78fb623eb2e520667c6c2e484374a59d6ff33989b2253c0f", "1.10.0--r42hdfd78af_0": "sha256:187435ab02e47e19fd7e0f224686d157a66a5707c0462deebfac102d0e48a00b", "1.12.0--r43hdfd78af_0": "sha256:baf768f23182d890ff3eb5bdedf9bedfe0b54f23ee1001cd1473b4f04057cbd4", "1.14.0--r43hdfd78af_0": "sha256:b526c6242e4d977a9b2cbb43ba9cf9fd5e8fb2c0bb7bbf9f342073998cc9f6e1"}, "docker": "quay.io/biocontainers/bioconductor-regutools", "aliases": {"Cytoscape": "/usr/local/bin/Cytoscape", "cytoscape.sh": "/usr/local/bin/cytoscape.sh", "gen_vmoptions.sh": "/usr/local/bin/gen_vmoptions.sh", "curve_keygen": "/usr/local/bin/curve_keygen", "jaotc": "/usr/local/bin/jaotc", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-regutools.
shpc-registry automated BioContainers addition for bioconductor-regutools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-regutools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-regutools:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-regutools/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-regutools/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-regutools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regutools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regutools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-regutools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-regutools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-regutools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cytoscape

```bash
$ singularity exec <container> /usr/local/bin/Cytoscape
$ podman run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cytoscape.sh

```bash
$ singularity exec <container> /usr/local/bin/cytoscape.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_vmoptions.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_vmoptions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
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