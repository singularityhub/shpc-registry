---
layout: container
name:  "quay.io/biocontainers/pymvpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymvpa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pymvpa/container.yaml"
updated_at: "2022-10-27 00:41:22.154761"
latest: "2.6.5--py39h70e0db4_5"
container_url: "https://biocontainers.pro/tools/pymvpa"
aliases:
 - "nib-conform"
 - "nib-dicomfs"
 - "nib-diff"
 - "nib-ls"
 - "nib-nifti-dx"
 - "nib-roi"
 - "nib-stats"
 - "nib-tck2trk"
 - "nib-trk2tck"
 - "parrec2nii"
versions:
 - "2.6.5--py39h70e0db4_5"
description: "shpc-registry automated BioContainers addition for pymvpa"
config: {"url": "https://biocontainers.pro/tools/pymvpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymvpa", "latest": {"2.6.5--py39h70e0db4_5": "sha256:8511e0b9e2e8bfb7fdb8b67b23e4b0baf71a91f61a8d76dfd9c9e8d29795179c"}, "tags": {"2.6.5--py39h70e0db4_5": "sha256:8511e0b9e2e8bfb7fdb8b67b23e4b0baf71a91f61a8d76dfd9c9e8d29795179c"}, "docker": "quay.io/biocontainers/pymvpa", "aliases": {"nib-conform": "/usr/local/bin/nib-conform", "nib-dicomfs": "/usr/local/bin/nib-dicomfs", "nib-diff": "/usr/local/bin/nib-diff", "nib-ls": "/usr/local/bin/nib-ls", "nib-nifti-dx": "/usr/local/bin/nib-nifti-dx", "nib-roi": "/usr/local/bin/nib-roi", "nib-stats": "/usr/local/bin/nib-stats", "nib-tck2trk": "/usr/local/bin/nib-tck2trk", "nib-trk2tck": "/usr/local/bin/nib-trk2tck", "parrec2nii": "/usr/local/bin/parrec2nii"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymvpa.
shpc-registry automated BioContainers addition for pymvpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymvpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymvpa:2.6.5--py39h70e0db4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymvpa/2.6.5--py39h70e0db4_5
$ module help quay.io/biocontainers/pymvpa/2.6.5--py39h70e0db4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymvpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymvpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymvpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymvpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymvpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymvpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nib-conform

```bash
$ singularity exec <container> /usr/local/bin/nib-conform
$ podman run --it --rm --entrypoint /usr/local/bin/nib-conform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-conform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-dicomfs

```bash
$ singularity exec <container> /usr/local/bin/nib-dicomfs
$ podman run --it --rm --entrypoint /usr/local/bin/nib-dicomfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-dicomfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-diff

```bash
$ singularity exec <container> /usr/local/bin/nib-diff
$ podman run --it --rm --entrypoint /usr/local/bin/nib-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-ls

```bash
$ singularity exec <container> /usr/local/bin/nib-ls
$ podman run --it --rm --entrypoint /usr/local/bin/nib-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-nifti-dx

```bash
$ singularity exec <container> /usr/local/bin/nib-nifti-dx
$ podman run --it --rm --entrypoint /usr/local/bin/nib-nifti-dx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-nifti-dx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-roi

```bash
$ singularity exec <container> /usr/local/bin/nib-roi
$ podman run --it --rm --entrypoint /usr/local/bin/nib-roi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-roi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-stats

```bash
$ singularity exec <container> /usr/local/bin/nib-stats
$ podman run --it --rm --entrypoint /usr/local/bin/nib-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-tck2trk

```bash
$ singularity exec <container> /usr/local/bin/nib-tck2trk
$ podman run --it --rm --entrypoint /usr/local/bin/nib-tck2trk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-tck2trk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-trk2tck

```bash
$ singularity exec <container> /usr/local/bin/nib-trk2tck
$ podman run --it --rm --entrypoint /usr/local/bin/nib-trk2tck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-trk2tck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parrec2nii

```bash
$ singularity exec <container> /usr/local/bin/parrec2nii
$ podman run --it --rm --entrypoint /usr/local/bin/parrec2nii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parrec2nii   -v ${PWD} -w ${PWD} <container> -c " $@"
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