---
layout: container
name:  "quay.io/biocontainers/enzbert"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enzbert/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enzbert/container.yaml"
updated_at: "2025-11-18 03:32:56.753068"
latest: "1.1--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/enzbert"
aliases:
 - "compare_gos.py"
 - "enzbert"
 - "go_plot.py"
 - "ncbi_gene_results_to_python.py"
 - "prt_terms.py"
 - "sacremoses"
 - "streamlit"
 - "streamlit.cmd"
 - "transformers-cli"
 - "wr_hier.py"
 - "wr_sections.py"
 - "fetch_associations.py"
 - "find_enrichment.py"
 - "map_to_slim.py"
 - "plot_go_term.py"
 - "watchmedo"
 - "plasma-store-server"
 - "plasma_store"
 - "dask"
 - "ninja"
 - "imageio_download_bin"
 - "imageio_remove_bin"
 - "lsm2bin"
 - "skivi"
 - "tifffile"
 - "vba_extract.py"
 - "sha256_profile"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
versions:
 - "1.1--pyh7e72e81_0"
description: "singularity registry hpc automated addition for enzbert"
config: {"url": "https://biocontainers.pro/tools/enzbert", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for enzbert", "latest": {"1.1--pyh7e72e81_0": "sha256:d41e2e49173ecf0219da4c81f04ad9fdd71a2b40a6d8396090bc38f86067a169"}, "tags": {"1.1--pyh7e72e81_0": "sha256:d41e2e49173ecf0219da4c81f04ad9fdd71a2b40a6d8396090bc38f86067a169"}, "docker": "quay.io/biocontainers/enzbert", "aliases": {"compare_gos.py": "/usr/local/bin/compare_gos.py", "enzbert": "/usr/local/bin/enzbert", "go_plot.py": "/usr/local/bin/go_plot.py", "ncbi_gene_results_to_python.py": "/usr/local/bin/ncbi_gene_results_to_python.py", "prt_terms.py": "/usr/local/bin/prt_terms.py", "sacremoses": "/usr/local/bin/sacremoses", "streamlit": "/usr/local/bin/streamlit", "streamlit.cmd": "/usr/local/bin/streamlit.cmd", "transformers-cli": "/usr/local/bin/transformers-cli", "wr_hier.py": "/usr/local/bin/wr_hier.py", "wr_sections.py": "/usr/local/bin/wr_sections.py", "fetch_associations.py": "/usr/local/bin/fetch_associations.py", "find_enrichment.py": "/usr/local/bin/find_enrichment.py", "map_to_slim.py": "/usr/local/bin/map_to_slim.py", "plot_go_term.py": "/usr/local/bin/plot_go_term.py", "watchmedo": "/usr/local/bin/watchmedo", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "dask": "/usr/local/bin/dask", "ninja": "/usr/local/bin/ninja", "imageio_download_bin": "/usr/local/bin/imageio_download_bin", "imageio_remove_bin": "/usr/local/bin/imageio_remove_bin", "lsm2bin": "/usr/local/bin/lsm2bin", "skivi": "/usr/local/bin/skivi", "tifffile": "/usr/local/bin/tifffile", "vba_extract.py": "/usr/local/bin/vba_extract.py", "sha256_profile": "/usr/local/bin/sha256_profile", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enzbert.
singularity registry hpc automated addition for enzbert
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enzbert
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enzbert:1.1--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enzbert/1.1--pyh7e72e81_0
$ module help quay.io/biocontainers/enzbert/1.1--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enzbert-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enzbert-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enzbert-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enzbert-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enzbert-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enzbert-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_gos.py

```bash
$ singularity exec <container> /usr/local/bin/compare_gos.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enzbert

```bash
$ singularity exec <container> /usr/local/bin/enzbert
$ podman run --it --rm --entrypoint /usr/local/bin/enzbert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enzbert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go_plot.py

```bash
$ singularity exec <container> /usr/local/bin/go_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_gene_results_to_python.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_gene_results_to_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prt_terms.py

```bash
$ singularity exec <container> /usr/local/bin/prt_terms.py
$ podman run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sacremoses

```bash
$ singularity exec <container> /usr/local/bin/sacremoses
$ podman run --it --rm --entrypoint /usr/local/bin/sacremoses   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sacremoses   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit

```bash
$ singularity exec <container> /usr/local/bin/streamlit
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit.cmd

```bash
$ singularity exec <container> /usr/local/bin/streamlit.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers-cli

```bash
$ singularity exec <container> /usr/local/bin/transformers-cli
$ podman run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_hier.py

```bash
$ singularity exec <container> /usr/local/bin/wr_hier.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_sections.py

```bash
$ singularity exec <container> /usr/local/bin/wr_sections.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_associations.py

```bash
$ singularity exec <container> /usr/local/bin/fetch_associations.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_enrichment.py

```bash
$ singularity exec <container> /usr/local/bin/find_enrichment.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_to_slim.py

```bash
$ singularity exec <container> /usr/local/bin/map_to_slim.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_go_term.py

```bash
$ singularity exec <container> /usr/local/bin/plot_go_term.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchmedo

```bash
$ singularity exec <container> /usr/local/bin/watchmedo
$ podman run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imageio_download_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_download_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imageio_remove_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_remove_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsm2bin

```bash
$ singularity exec <container> /usr/local/bin/lsm2bin
$ podman run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skivi

```bash
$ singularity exec <container> /usr/local/bin/skivi
$ podman run --it --rm --entrypoint /usr/local/bin/skivi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skivi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tifffile

```bash
$ singularity exec <container> /usr/local/bin/tifffile
$ podman run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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