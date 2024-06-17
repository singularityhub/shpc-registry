---
layout: container
name:  "quay.io/biocontainers/bioconductor-msnbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msnbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msnbase/container.yaml"
updated_at: "2024-06-17 02:50:23.084953"
latest: "2.28.1--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-msnbase"
aliases:
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
 - "hdf2gif"
 - "hdf2jpeg"
 - "hdf8to24"
 - "hdfcomp"
versions:
 - "2.8.3--r351hf484d3e_0"
 - "2.24.0--r42hc247a5b_0"
 - "2.20.4--r41hc247a5b_1"
 - "2.18.0--r41h399db7b_0"
 - "2.16.1--r40h399db7b_0"
 - "2.14.1--r40h5f743cb_0"
 - "2.24.0--r42hf17093f_1"
 - "2.26.0--r43hf17093f_0"
 - "2.28.1--r43hf17093f_0"
 - "2.28.1--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-msnbase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msnbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msnbase", "latest": {"2.28.1--r43hf17093f_1": "sha256:44cb05095737488995ad2e282534b7b52b9d3a0aa1211c5a1bee0a8fc7bf4aa3"}, "tags": {"2.8.3--r351hf484d3e_0": "sha256:ebd9244ae1e2ab403fb72cf47a83c3055c39e243a7249d4f90835a3e5b0597b3", "2.24.0--r42hc247a5b_0": "sha256:aeffe7cf3115a809dca214bf0095357cb530f25b452616ee34101318ea0dde88", "2.20.4--r41hc247a5b_1": "sha256:236e22f2c3c3887340d531fa3ccbd07b74c85a20800e9e387b7a188d28bb2213", "2.18.0--r41h399db7b_0": "sha256:863b2f8e694a58b1eec7776555a9a8c26539e32cfb0337f3d7bebc217295d7a4", "2.16.1--r40h399db7b_0": "sha256:492fa2735882e1355432efec60750b4652b1582a60038b945350996fc51b41a3", "2.14.1--r40h5f743cb_0": "sha256:ec63bcc7e55a5e1a3a7f2cfd633e86b0e29eaca548b1fbd211a059d6d37a50e8", "2.24.0--r42hf17093f_1": "sha256:dbff7f4b167cb3d208cfe5bbec1c146a17389074519d982f16f9b5aafb85bbd1", "2.26.0--r43hf17093f_0": "sha256:08c6a50e08ca3d7728a0bf5f499145570a691b089a06f57ef25a023a76cc81c4", "2.28.1--r43hf17093f_0": "sha256:675d42b8c1555f2fc147c5af6cab98d6b3f4c334f84a1d261f2df620cdd23c65", "2.28.1--r43hf17093f_1": "sha256:44cb05095737488995ad2e282534b7b52b9d3a0aa1211c5a1bee0a8fc7bf4aa3"}, "docker": "quay.io/biocontainers/bioconductor-msnbase", "aliases": {"gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msnbase.
shpc-registry automated BioContainers addition for bioconductor-msnbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msnbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msnbase:2.28.1--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msnbase/2.28.1--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-msnbase/2.28.1--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msnbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msnbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msnbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msnbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msnbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msnbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2gif

```bash
$ singularity exec <container> /usr/local/bin/hdf2gif
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2jpeg

```bash
$ singularity exec <container> /usr/local/bin/hdf2jpeg
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf8to24

```bash
$ singularity exec <container> /usr/local/bin/hdf8to24
$ podman run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfcomp

```bash
$ singularity exec <container> /usr/local/bin/hdfcomp
$ podman run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
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