---
layout: container
name:  "quay.io/biocontainers/genewalk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genewalk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genewalk/container.yaml"
updated_at: "2024-08-08 03:25:29.176101"
latest: "1.6.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/genewalk"
aliases:
 - "compare_gos.py"
 - "fetch_associations.py"
 - "find_enrichment.py"
 - "genewalk"
 - "go_plot.py"
 - "map_to_slim.py"
 - "ncbi_gene_results_to_python.py"
 - "plot_go_term.py"
 - "prt_terms.py"
 - "wr_hier.py"
 - "wr_sections.py"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
 - "glacier"
versions:
 - "1.5.3--pyh5e36f6f_0"
 - "1.6.1--pyh7cba7a3_0"
 - "1.6.2--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for genewalk"
config: {"url": "https://biocontainers.pro/tools/genewalk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genewalk", "latest": {"1.6.2--pyh7cba7a3_0": "sha256:abc7d78a3fabc5e1359e0c5a78bd1dbb7f746a6cd3a0e011f11a15ac3d4be5a0"}, "tags": {"1.5.3--pyh5e36f6f_0": "sha256:fe6cc3d5a6ba40d01ff10a54ba06fcf3ec3a689299e922ab9bfe3fcdd8183acf", "1.6.1--pyh7cba7a3_0": "sha256:e67fec9e237f69e16285a553f6d81c6f212d498d692159123fbb25e844adff3d", "1.6.2--pyh7cba7a3_0": "sha256:abc7d78a3fabc5e1359e0c5a78bd1dbb7f746a6cd3a0e011f11a15ac3d4be5a0"}, "docker": "quay.io/biocontainers/genewalk", "aliases": {"compare_gos.py": "/usr/local/bin/compare_gos.py", "fetch_associations.py": "/usr/local/bin/fetch_associations.py", "find_enrichment.py": "/usr/local/bin/find_enrichment.py", "genewalk": "/usr/local/bin/genewalk", "go_plot.py": "/usr/local/bin/go_plot.py", "map_to_slim.py": "/usr/local/bin/map_to_slim.py", "ncbi_gene_results_to_python.py": "/usr/local/bin/ncbi_gene_results_to_python.py", "plot_go_term.py": "/usr/local/bin/plot_go_term.py", "prt_terms.py": "/usr/local/bin/prt_terms.py", "wr_hier.py": "/usr/local/bin/wr_hier.py", "wr_sections.py": "/usr/local/bin/wr_sections.py", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genewalk.
shpc-registry automated BioContainers addition for genewalk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genewalk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genewalk:1.6.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genewalk/1.6.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/genewalk/1.6.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genewalk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genewalk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genewalk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genewalk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genewalk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genewalk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_gos.py

```bash
$ singularity exec <container> /usr/local/bin/compare_gos.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### genewalk

```bash
$ singularity exec <container> /usr/local/bin/genewalk
$ podman run --it --rm --entrypoint /usr/local/bin/genewalk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genewalk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go_plot.py

```bash
$ singularity exec <container> /usr/local/bin/go_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_to_slim.py

```bash
$ singularity exec <container> /usr/local/bin/map_to_slim.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_gene_results_to_python.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_gene_results_to_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_go_term.py

```bash
$ singularity exec <container> /usr/local/bin/plot_go_term.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prt_terms.py

```bash
$ singularity exec <container> /usr/local/bin/prt_terms.py
$ podman run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glacier

```bash
$ singularity exec <container> /usr/local/bin/glacier
$ podman run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
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