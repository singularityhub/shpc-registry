---
layout: container
name:  "quay.io/biocontainers/pymvpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymvpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymvpa/container.yaml"
updated_at: "2023-07-06 03:07:08.564258"
latest: "2.6.5--py310hda10691_8"
container_url: "https://biocontainers.pro/tools/pymvpa"
aliases:
 - "ccache-swig"
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
 - "swig"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "xkbcli"
 - "pg_config"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
versions:
 - "2.6.5--py39h70e0db4_5"
 - "2.6.5--py310hda10691_8"
description: "shpc-registry automated BioContainers addition for pymvpa"
config: {"url": "https://biocontainers.pro/tools/pymvpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymvpa", "latest": {"2.6.5--py310hda10691_8": "sha256:5122c074b0aad966b8f212f48c4bd86a1a1eed67d173ac5b18569a4fc2dab848"}, "tags": {"2.6.5--py39h70e0db4_5": "sha256:8511e0b9e2e8bfb7fdb8b67b23e4b0baf71a91f61a8d76dfd9c9e8d29795179c", "2.6.5--py310hda10691_8": "sha256:5122c074b0aad966b8f212f48c4bd86a1a1eed67d173ac5b18569a4fc2dab848"}, "docker": "quay.io/biocontainers/pymvpa", "aliases": {"ccache-swig": "/usr/local/bin/ccache-swig", "nib-conform": "/usr/local/bin/nib-conform", "nib-dicomfs": "/usr/local/bin/nib-dicomfs", "nib-diff": "/usr/local/bin/nib-diff", "nib-ls": "/usr/local/bin/nib-ls", "nib-nifti-dx": "/usr/local/bin/nib-nifti-dx", "nib-roi": "/usr/local/bin/nib-roi", "nib-stats": "/usr/local/bin/nib-stats", "nib-tck2trk": "/usr/local/bin/nib-tck2trk", "nib-trk2tck": "/usr/local/bin/nib-trk2tck", "parrec2nii": "/usr/local/bin/parrec2nii", "swig": "/usr/local/bin/swig", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "xkbcli": "/usr/local/bin/xkbcli", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymvpa.
shpc-registry automated BioContainers addition for pymvpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymvpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymvpa:2.6.5--py310hda10691_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymvpa/2.6.5--py310hda10691_8
$ module help quay.io/biocontainers/pymvpa/2.6.5--py310hda10691_8
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


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvkgen

```bash
$ singularity exec <container> /usr/local/bin/qvkgen
$ podman run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nspr-config

```bash
$ singularity exec <container> /usr/local/bin/nspr-config
$ podman run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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