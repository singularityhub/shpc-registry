---
layout: container
name:  "quay.io/biocontainers/oddsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oddsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oddsnp/container.yaml"
updated_at: "2026-07-01 07:10:07.299139"
latest: "0.1.1--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/oddsnp"
aliases:
 - "GTbarcode"
 - "cellsnp-lite"
 - "choreo_diagnose"
 - "choreo_get_chrome"
 - "kaleido_get_chrome"
 - "kaleido_mocker"
 - "oddSNP"
 - "vireo"
 - "debugpy-adapter"
 - "debugpy"
 - "plotly_get_chrome"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "curve_keygen"
 - "ref-cache"
 - "ipython3"
 - "ipython"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "annot-tsv"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
versions:
 - "0.1.1--pyh106432d_0"
description: "singularity registry hpc automated addition for oddsnp"
config: {"url": "https://biocontainers.pro/tools/oddsnp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for oddsnp", "latest": {"0.1.1--pyh106432d_0": "sha256:b38beba654fdb0b8afcc139ec5af82356ec24eaa95b54360ec75202f5d8119fc"}, "tags": {"0.1.1--pyh106432d_0": "sha256:b38beba654fdb0b8afcc139ec5af82356ec24eaa95b54360ec75202f5d8119fc"}, "docker": "quay.io/biocontainers/oddsnp", "aliases": {"GTbarcode": "/usr/local/bin/GTbarcode", "cellsnp-lite": "/usr/local/bin/cellsnp-lite", "choreo_diagnose": "/usr/local/bin/choreo_diagnose", "choreo_get_chrome": "/usr/local/bin/choreo_get_chrome", "kaleido_get_chrome": "/usr/local/bin/kaleido_get_chrome", "kaleido_mocker": "/usr/local/bin/kaleido_mocker", "oddSNP": "/usr/local/bin/oddSNP", "vireo": "/usr/local/bin/vireo", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "debugpy": "/usr/local/bin/debugpy", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "curve_keygen": "/usr/local/bin/curve_keygen", "ref-cache": "/usr/local/bin/ref-cache", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "annot-tsv": "/usr/local/bin/annot-tsv", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oddsnp.
singularity registry hpc automated addition for oddsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oddsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oddsnp:0.1.1--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oddsnp/0.1.1--pyh106432d_0
$ module help quay.io/biocontainers/oddsnp/0.1.1--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oddsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oddsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oddsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oddsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oddsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oddsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GTbarcode

```bash
$ singularity exec <container> /usr/local/bin/GTbarcode
$ podman run --it --rm --entrypoint /usr/local/bin/GTbarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GTbarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cellsnp-lite

```bash
$ singularity exec <container> /usr/local/bin/cellsnp-lite
$ podman run --it --rm --entrypoint /usr/local/bin/cellsnp-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cellsnp-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choreo_diagnose

```bash
$ singularity exec <container> /usr/local/bin/choreo_diagnose
$ podman run --it --rm --entrypoint /usr/local/bin/choreo_diagnose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choreo_diagnose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choreo_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/choreo_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/choreo_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choreo_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/kaleido_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido_mocker

```bash
$ singularity exec <container> /usr/local/bin/kaleido_mocker
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido_mocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido_mocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oddSNP

```bash
$ singularity exec <container> /usr/local/bin/oddSNP
$ podman run --it --rm --entrypoint /usr/local/bin/oddSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oddSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vireo

```bash
$ singularity exec <container> /usr/local/bin/vireo
$ podman run --it --rm --entrypoint /usr/local/bin/vireo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vireo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
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