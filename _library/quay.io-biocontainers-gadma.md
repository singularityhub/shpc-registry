---
layout: container
name:  "quay.io/biocontainers/gadma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gadma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gadma/container.yaml"
updated_at: "2024-11-18 16:32:02.413030"
latest: "2.0.0rc26--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gadma"
aliases:
 - "demes"
 - "gadma"
 - "gadma-get_confidence_intervals"
 - "gadma-get_confidence_intervals_for_ld"
 - "gadma-precompute_ld_data"
 - "gadma-run_ls_on_boot_data"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "bokeh"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.8"
versions:
 - "2.0.0rc22--pyhdfd78af_0"
 - "2.0.0rc23--pyhdfd78af_0"
 - "2.0.0rc25--pyhdfd78af_0"
 - "2.0.0rc26--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for gadma"
config: {"url": "https://biocontainers.pro/tools/gadma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gadma", "latest": {"2.0.0rc26--pyhdfd78af_0": "sha256:064e4dc7ef7bb3445eed411090c01fbd286076213a10ce9a62829b61ad14ab3d"}, "tags": {"2.0.0rc22--pyhdfd78af_0": "sha256:d8156f1ec8ec4ed9d055a9340842069afa23ce5c3d24076e907de781d5731d74", "2.0.0rc23--pyhdfd78af_0": "sha256:7491eb9854ae7e776c024848e5ccd7b64842c790877cf266ac01e87e4c408a51", "2.0.0rc25--pyhdfd78af_0": "sha256:ff944a1c46baa57c565d892133cf4e320ce5700600dcb711366e3d1cfdf62cf0", "2.0.0rc26--pyhdfd78af_0": "sha256:064e4dc7ef7bb3445eed411090c01fbd286076213a10ce9a62829b61ad14ab3d"}, "docker": "quay.io/biocontainers/gadma", "aliases": {"demes": "/usr/local/bin/demes", "gadma": "/usr/local/bin/gadma", "gadma-get_confidence_intervals": "/usr/local/bin/gadma-get_confidence_intervals", "gadma-get_confidence_intervals_for_ld": "/usr/local/bin/gadma-get_confidence_intervals_for_ld", "gadma-precompute_ld_data": "/usr/local/bin/gadma-precompute_ld_data", "gadma-run_ls_on_boot_data": "/usr/local/bin/gadma-run_ls_on_boot_data", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "bokeh": "/usr/local/bin/bokeh", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.8": "/usr/local/bin/f2py3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gadma.
shpc-registry automated BioContainers addition for gadma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gadma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gadma:2.0.0rc26--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gadma/2.0.0rc26--pyhdfd78af_0
$ module help quay.io/biocontainers/gadma/2.0.0rc26--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gadma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gadma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gadma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gadma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gadma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gadma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### demes

```bash
$ singularity exec <container> /usr/local/bin/demes
$ podman run --it --rm --entrypoint /usr/local/bin/demes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gadma

```bash
$ singularity exec <container> /usr/local/bin/gadma
$ podman run --it --rm --entrypoint /usr/local/bin/gadma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gadma-get_confidence_intervals

```bash
$ singularity exec <container> /usr/local/bin/gadma-get_confidence_intervals
$ podman run --it --rm --entrypoint /usr/local/bin/gadma-get_confidence_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadma-get_confidence_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gadma-get_confidence_intervals_for_ld

```bash
$ singularity exec <container> /usr/local/bin/gadma-get_confidence_intervals_for_ld
$ podman run --it --rm --entrypoint /usr/local/bin/gadma-get_confidence_intervals_for_ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadma-get_confidence_intervals_for_ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gadma-precompute_ld_data

```bash
$ singularity exec <container> /usr/local/bin/gadma-precompute_ld_data
$ podman run --it --rm --entrypoint /usr/local/bin/gadma-precompute_ld_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadma-precompute_ld_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gadma-run_ls_on_boot_data

```bash
$ singularity exec <container> /usr/local/bin/gadma-run_ls_on_boot_data
$ podman run --it --rm --entrypoint /usr/local/bin/gadma-run_ls_on_boot_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadma-run_ls_on_boot_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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