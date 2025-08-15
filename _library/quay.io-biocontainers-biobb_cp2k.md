---
layout: container
name:  "quay.io/biocontainers/biobb_cp2k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_cp2k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_cp2k/container.yaml"
updated_at: "2025-08-15 05:10:17.124768"
latest: "4.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_cp2k"
aliases:
 - "cp2k.sopt"
 - "cp2k.ssmp"
 - "cp2k_prep"
 - "cp2k_run"
 - "cp2k_shell.ssmp"
 - "libxsmm_gemm_generator"
 - "fftw-wisdom"
 - "fftw-wisdom-to-conf"
 - "fftwf-wisdom"
 - "fftwl-wisdom"
 - "normalizer"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "3.9.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for biobb_cp2k"
config: {"url": "https://biocontainers.pro/tools/biobb_cp2k", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobb_cp2k", "latest": {"4.1.0--pyhdfd78af_0": "sha256:a9d6fc6cac4a78d7998d73f1ddf6a487f18948de06457a4f15b217bbda6a1c89"}, "tags": {"3.9.0--pyhdfd78af_0": "sha256:a032471dd36b83804471689191428493185dac578b8452465c3dc73f24b820e6", "4.0.0--pyhdfd78af_0": "sha256:eb9269cb9547ad28813885349b5066a33f76dc18f40ea2487394223936c12b8c", "4.1.0--pyhdfd78af_0": "sha256:a9d6fc6cac4a78d7998d73f1ddf6a487f18948de06457a4f15b217bbda6a1c89"}, "docker": "quay.io/biocontainers/biobb_cp2k", "aliases": {"cp2k.sopt": "/usr/local/bin/cp2k.sopt", "cp2k.ssmp": "/usr/local/bin/cp2k.ssmp", "cp2k_prep": "/usr/local/bin/cp2k_prep", "cp2k_run": "/usr/local/bin/cp2k_run", "cp2k_shell.ssmp": "/usr/local/bin/cp2k_shell.ssmp", "libxsmm_gemm_generator": "/usr/local/bin/libxsmm_gemm_generator", "fftw-wisdom": "/usr/local/bin/fftw-wisdom", "fftw-wisdom-to-conf": "/usr/local/bin/fftw-wisdom-to-conf", "fftwf-wisdom": "/usr/local/bin/fftwf-wisdom", "fftwl-wisdom": "/usr/local/bin/fftwl-wisdom", "normalizer": "/usr/local/bin/normalizer", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_cp2k.
singularity registry hpc automated addition for biobb_cp2k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_cp2k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_cp2k:4.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_cp2k/4.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_cp2k/4.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_cp2k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_cp2k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_cp2k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_cp2k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_cp2k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_cp2k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cp2k.sopt

```bash
$ singularity exec <container> /usr/local/bin/cp2k.sopt
$ podman run --it --rm --entrypoint /usr/local/bin/cp2k.sopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp2k.sopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.ssmp

```bash
$ singularity exec <container> /usr/local/bin/cp2k.ssmp
$ podman run --it --rm --entrypoint /usr/local/bin/cp2k.ssmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp2k.ssmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k_prep

```bash
$ singularity exec <container> /usr/local/bin/cp2k_prep
$ podman run --it --rm --entrypoint /usr/local/bin/cp2k_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp2k_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k_run

```bash
$ singularity exec <container> /usr/local/bin/cp2k_run
$ podman run --it --rm --entrypoint /usr/local/bin/cp2k_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp2k_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k_shell.ssmp

```bash
$ singularity exec <container> /usr/local/bin/cp2k_shell.ssmp
$ podman run --it --rm --entrypoint /usr/local/bin/cp2k_shell.ssmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp2k_shell.ssmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libxsmm_gemm_generator

```bash
$ singularity exec <container> /usr/local/bin/libxsmm_gemm_generator
$ podman run --it --rm --entrypoint /usr/local/bin/libxsmm_gemm_generator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libxsmm_gemm_generator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftw-wisdom-to-conf

```bash
$ singularity exec <container> /usr/local/bin/fftw-wisdom-to-conf
$ podman run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftw-wisdom-to-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwf-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwf-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwf-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftwl-wisdom

```bash
$ singularity exec <container> /usr/local/bin/fftwl-wisdom
$ podman run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftwl-wisdom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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