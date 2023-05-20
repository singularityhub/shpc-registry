---
layout: container
name:  "quay.io/biocontainers/deblur"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deblur/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deblur/container.yaml"
updated_at: "2023-05-20 02:35:09.926938"
latest: "1.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/deblur"
aliases:
 - "deblur"
 - "indexdb_rna"
 - "sortmerna"
 - "biom"
 - "vsearch"
 - "doesitcache"
 - "ipython3"
 - "ipython"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
versions:
 - "1.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for deblur"
config: {"url": "https://biocontainers.pro/tools/deblur", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deblur", "latest": {"1.1.1--pyhdfd78af_0": "sha256:c0f007e678e948344c754acef6c61b1062e1a7d69136cc68cc9d75db7709d3a8"}, "tags": {"1.1.1--pyhdfd78af_0": "sha256:c0f007e678e948344c754acef6c61b1062e1a7d69136cc68cc9d75db7709d3a8"}, "docker": "quay.io/biocontainers/deblur", "aliases": {"deblur": "/usr/local/bin/deblur", "indexdb_rna": "/usr/local/bin/indexdb_rna", "sortmerna": "/usr/local/bin/sortmerna", "biom": "/usr/local/bin/biom", "vsearch": "/usr/local/bin/vsearch", "doesitcache": "/usr/local/bin/doesitcache", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deblur.
shpc-registry automated BioContainers addition for deblur
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deblur
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deblur:1.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deblur/1.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/deblur/1.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deblur-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deblur-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deblur-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deblur-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deblur-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deblur-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deblur

```bash
$ singularity exec <container> /usr/local/bin/deblur
$ podman run --it --rm --entrypoint /usr/local/bin/deblur   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deblur   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_rna

```bash
$ singularity exec <container> /usr/local/bin/indexdb_rna
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortmerna

```bash
$ singularity exec <container> /usr/local/bin/sortmerna
$ podman run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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