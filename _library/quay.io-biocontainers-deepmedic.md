---
layout: container
name:  "quay.io/biocontainers/deepmedic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepmedic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepmedic/container.yaml"
updated_at: "2023-05-03 02:58:36.641953"
latest: "0.6.1--py_1"
container_url: "https://biocontainers.pro/tools/deepmedic"
aliases:
 - "deepMedicRun"
 - "nib-dicomfs"
 - "nib-diff"
 - "nib-ls"
 - "nib-nifti-dx"
 - "nib-tck2trk"
 - "nib-trk2tck"
 - "parrec2nii"
 - "ppserver.py"
 - "unit2"
 - "theano-cache"
 - "theano-nose"
 - "mako-render"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
versions:
 - "0.6.1--py_1"
description: "shpc-registry automated BioContainers addition for deepmedic"
config: {"url": "https://biocontainers.pro/tools/deepmedic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepmedic", "latest": {"0.6.1--py_1": "sha256:55a808db7aeac123986cd1624bacfe4dd25442aa71302965e32d14cef8138e64"}, "tags": {"0.6.1--py_1": "sha256:55a808db7aeac123986cd1624bacfe4dd25442aa71302965e32d14cef8138e64"}, "docker": "quay.io/biocontainers/deepmedic", "aliases": {"deepMedicRun": "/usr/local/bin/deepMedicRun", "nib-dicomfs": "/usr/local/bin/nib-dicomfs", "nib-diff": "/usr/local/bin/nib-diff", "nib-ls": "/usr/local/bin/nib-ls", "nib-nifti-dx": "/usr/local/bin/nib-nifti-dx", "nib-tck2trk": "/usr/local/bin/nib-tck2trk", "nib-trk2tck": "/usr/local/bin/nib-trk2tck", "parrec2nii": "/usr/local/bin/parrec2nii", "ppserver.py": "/usr/local/bin/ppserver.py", "unit2": "/usr/local/bin/unit2", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "mako-render": "/usr/local/bin/mako-render", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepmedic.
shpc-registry automated BioContainers addition for deepmedic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepmedic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepmedic:0.6.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepmedic/0.6.1--py_1
$ module help quay.io/biocontainers/deepmedic/0.6.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepmedic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepmedic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepmedic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepmedic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepmedic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepmedic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepMedicRun

```bash
$ singularity exec <container> /usr/local/bin/deepMedicRun
$ podman run --it --rm --entrypoint /usr/local/bin/deepMedicRun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepMedicRun   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ppserver.py

```bash
$ singularity exec <container> /usr/local/bin/ppserver.py
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unit2

```bash
$ singularity exec <container> /usr/local/bin/unit2
$ podman run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-cache

```bash
$ singularity exec <container> /usr/local/bin/theano-cache
$ podman run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-nose

```bash
$ singularity exec <container> /usr/local/bin/theano-nose
$ podman run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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