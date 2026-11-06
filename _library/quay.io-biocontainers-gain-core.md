---
layout: container
name:  "quay.io/biocontainers/gain-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gain-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gain-core/container.yaml"
updated_at: "2026-11-06 18:30:41.245049"
latest: "2026.10.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gain-core"
aliases:
 - "annotate_doc"
 - "annotate_tabular"
 - "annotate_variant_effects"
 - "annotate_variant_effects_vcf"
 - "annotate_vcf"
 - "apsw"
 - "binning_tool"
 - "binning_tool_view"
 - "demo_graphs_cli"
 - "draw_score_histograms"
 - "grr_browse"
 - "grr_cache_repo"
 - "grr_manage"
 - "markdown2"
 - "prepare_tabular"
 - "to_gpf_gene_models_format"
 - "inv"
 - "invoke"
 - "session-info2"
 - "session-info"
 - "cffi-gen-src"
 - "wsdump"
 - "zarr"
 - "dotenv"
 - "dask"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "idna"
 - "h2benchmark"
 - "jp.py"
 - "fc-genconf"
 - "checksum-profile"
 - "elasticurl"
 - "natsort"
 - "h5delete"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
versions:
 - "2026.10.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gain-core"
config: {"url": "https://biocontainers.pro/tools/gain-core", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gain-core", "latest": {"2026.10.2--pyhdfd78af_0": "sha256:7ffc38d8d34bceab52c5fa2d67d2c6ddfc2fa6ca0a83dc417c82b71ff0382016"}, "tags": {"2026.10.2--pyhdfd78af_0": "sha256:7ffc38d8d34bceab52c5fa2d67d2c6ddfc2fa6ca0a83dc417c82b71ff0382016"}, "docker": "quay.io/biocontainers/gain-core", "aliases": {"annotate_doc": "/usr/local/bin/annotate_doc", "annotate_tabular": "/usr/local/bin/annotate_tabular", "annotate_variant_effects": "/usr/local/bin/annotate_variant_effects", "annotate_variant_effects_vcf": "/usr/local/bin/annotate_variant_effects_vcf", "annotate_vcf": "/usr/local/bin/annotate_vcf", "apsw": "/usr/local/bin/apsw", "binning_tool": "/usr/local/bin/binning_tool", "binning_tool_view": "/usr/local/bin/binning_tool_view", "demo_graphs_cli": "/usr/local/bin/demo_graphs_cli", "draw_score_histograms": "/usr/local/bin/draw_score_histograms", "grr_browse": "/usr/local/bin/grr_browse", "grr_cache_repo": "/usr/local/bin/grr_cache_repo", "grr_manage": "/usr/local/bin/grr_manage", "markdown2": "/usr/local/bin/markdown2", "prepare_tabular": "/usr/local/bin/prepare_tabular", "to_gpf_gene_models_format": "/usr/local/bin/to_gpf_gene_models_format", "inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "session-info2": "/usr/local/bin/session-info2", "session-info": "/usr/local/bin/session-info", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "wsdump": "/usr/local/bin/wsdump", "zarr": "/usr/local/bin/zarr", "dotenv": "/usr/local/bin/dotenv", "dask": "/usr/local/bin/dask", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "idna": "/usr/local/bin/idna", "h2benchmark": "/usr/local/bin/h2benchmark", "jp.py": "/usr/local/bin/jp.py", "fc-genconf": "/usr/local/bin/fc-genconf", "checksum-profile": "/usr/local/bin/checksum-profile", "elasticurl": "/usr/local/bin/elasticurl", "natsort": "/usr/local/bin/natsort", "h5delete": "/usr/local/bin/h5delete", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gain-core.
singularity registry hpc automated addition for gain-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gain-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gain-core:2026.10.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gain-core/2026.10.2--pyhdfd78af_0
$ module help quay.io/biocontainers/gain-core/2026.10.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gain-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gain-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gain-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gain-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gain-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gain-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_doc

```bash
$ singularity exec <container> /usr/local/bin/annotate_doc
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_tabular

```bash
$ singularity exec <container> /usr/local/bin/annotate_tabular
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_variant_effects

```bash
$ singularity exec <container> /usr/local/bin/annotate_variant_effects
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_variant_effects   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_variant_effects   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_variant_effects_vcf

```bash
$ singularity exec <container> /usr/local/bin/annotate_variant_effects_vcf
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_variant_effects_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_variant_effects_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_vcf

```bash
$ singularity exec <container> /usr/local/bin/annotate_vcf
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### apsw

```bash
$ singularity exec <container> /usr/local/bin/apsw
$ podman run --it --rm --entrypoint /usr/local/bin/apsw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apsw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binning_tool

```bash
$ singularity exec <container> /usr/local/bin/binning_tool
$ podman run --it --rm --entrypoint /usr/local/bin/binning_tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binning_tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binning_tool_view

```bash
$ singularity exec <container> /usr/local/bin/binning_tool_view
$ podman run --it --rm --entrypoint /usr/local/bin/binning_tool_view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binning_tool_view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demo_graphs_cli

```bash
$ singularity exec <container> /usr/local/bin/demo_graphs_cli
$ podman run --it --rm --entrypoint /usr/local/bin/demo_graphs_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demo_graphs_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_score_histograms

```bash
$ singularity exec <container> /usr/local/bin/draw_score_histograms
$ podman run --it --rm --entrypoint /usr/local/bin/draw_score_histograms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_score_histograms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grr_browse

```bash
$ singularity exec <container> /usr/local/bin/grr_browse
$ podman run --it --rm --entrypoint /usr/local/bin/grr_browse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grr_browse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grr_cache_repo

```bash
$ singularity exec <container> /usr/local/bin/grr_cache_repo
$ podman run --it --rm --entrypoint /usr/local/bin/grr_cache_repo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grr_cache_repo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grr_manage

```bash
$ singularity exec <container> /usr/local/bin/grr_manage
$ podman run --it --rm --entrypoint /usr/local/bin/grr_manage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grr_manage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown2

```bash
$ singularity exec <container> /usr/local/bin/markdown2
$ podman run --it --rm --entrypoint /usr/local/bin/markdown2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_tabular

```bash
$ singularity exec <container> /usr/local/bin/prepare_tabular
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to_gpf_gene_models_format

```bash
$ singularity exec <container> /usr/local/bin/to_gpf_gene_models_format
$ podman run --it --rm --entrypoint /usr/local/bin/to_gpf_gene_models_format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to_gpf_gene_models_format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inv

```bash
$ singularity exec <container> /usr/local/bin/inv
$ podman run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invoke

```bash
$ singularity exec <container> /usr/local/bin/invoke
$ podman run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info2

```bash
$ singularity exec <container> /usr/local/bin/session-info2
$ podman run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info

```bash
$ singularity exec <container> /usr/local/bin/session-info
$ podman run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
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