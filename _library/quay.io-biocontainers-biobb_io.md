---
layout: container
name:  "quay.io/biocontainers/biobb_io"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_io/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_io/container.yaml"
updated_at: "2023-05-11 02:55:46.526213"
latest: "4.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_io"
aliases:
 - "alphafold"
 - "api_binding_site"
 - "canonical_fasta"
 - "drugbank"
 - "ideal_sdf"
 - "ligand"
 - "memprotmd_sim"
 - "memprotmd_sim_list"
 - "memprotmd_sim_search"
 - "mmcif"
 - "pdb"
 - "pdb_cluster_zip"
 - "pdb_variants"
 - "structure_info"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.8.0--pyhdfd78af_0"
 - "3.9.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_io"
config: {"url": "https://biocontainers.pro/tools/biobb_io", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_io", "latest": {"4.0.0--pyhdfd78af_0": "sha256:8810ccc0ed97b0f76f2cc7919254f115d8e8051a2df59cae1ea7fdad9c71ec6a"}, "tags": {"3.8.0--pyhdfd78af_0": "sha256:13301b1a4eba44ac98b4752e23035c338a962a34bd4add7b56233543255e1b94", "3.9.0--pyhdfd78af_0": "sha256:115d090a621475c2a8ee36334b14dd3533acd35401f2d77f9374552830332b62", "4.0.0--pyhdfd78af_0": "sha256:8810ccc0ed97b0f76f2cc7919254f115d8e8051a2df59cae1ea7fdad9c71ec6a"}, "docker": "quay.io/biocontainers/biobb_io", "aliases": {"alphafold": "/usr/local/bin/alphafold", "api_binding_site": "/usr/local/bin/api_binding_site", "canonical_fasta": "/usr/local/bin/canonical_fasta", "drugbank": "/usr/local/bin/drugbank", "ideal_sdf": "/usr/local/bin/ideal_sdf", "ligand": "/usr/local/bin/ligand", "memprotmd_sim": "/usr/local/bin/memprotmd_sim", "memprotmd_sim_list": "/usr/local/bin/memprotmd_sim_list", "memprotmd_sim_search": "/usr/local/bin/memprotmd_sim_search", "mmcif": "/usr/local/bin/mmcif", "pdb": "/usr/local/bin/pdb", "pdb_cluster_zip": "/usr/local/bin/pdb_cluster_zip", "pdb_variants": "/usr/local/bin/pdb_variants", "structure_info": "/usr/local/bin/structure_info", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_io.
shpc-registry automated BioContainers addition for biobb_io
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_io
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_io:4.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_io/4.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_io/4.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_io-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_io-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_io-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_io-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_io-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_io-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alphafold

```bash
$ singularity exec <container> /usr/local/bin/alphafold
$ podman run --it --rm --entrypoint /usr/local/bin/alphafold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alphafold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### api_binding_site

```bash
$ singularity exec <container> /usr/local/bin/api_binding_site
$ podman run --it --rm --entrypoint /usr/local/bin/api_binding_site   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/api_binding_site   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canonical_fasta

```bash
$ singularity exec <container> /usr/local/bin/canonical_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/canonical_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canonical_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drugbank

```bash
$ singularity exec <container> /usr/local/bin/drugbank
$ podman run --it --rm --entrypoint /usr/local/bin/drugbank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drugbank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ideal_sdf

```bash
$ singularity exec <container> /usr/local/bin/ideal_sdf
$ podman run --it --rm --entrypoint /usr/local/bin/ideal_sdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ideal_sdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ligand

```bash
$ singularity exec <container> /usr/local/bin/ligand
$ podman run --it --rm --entrypoint /usr/local/bin/ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memprotmd_sim

```bash
$ singularity exec <container> /usr/local/bin/memprotmd_sim
$ podman run --it --rm --entrypoint /usr/local/bin/memprotmd_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memprotmd_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memprotmd_sim_list

```bash
$ singularity exec <container> /usr/local/bin/memprotmd_sim_list
$ podman run --it --rm --entrypoint /usr/local/bin/memprotmd_sim_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memprotmd_sim_list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memprotmd_sim_search

```bash
$ singularity exec <container> /usr/local/bin/memprotmd_sim_search
$ podman run --it --rm --entrypoint /usr/local/bin/memprotmd_sim_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memprotmd_sim_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmcif

```bash
$ singularity exec <container> /usr/local/bin/mmcif
$ podman run --it --rm --entrypoint /usr/local/bin/mmcif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmcif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb

```bash
$ singularity exec <container> /usr/local/bin/pdb
$ podman run --it --rm --entrypoint /usr/local/bin/pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_cluster_zip

```bash
$ singularity exec <container> /usr/local/bin/pdb_cluster_zip
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_cluster_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_cluster_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_variants

```bash
$ singularity exec <container> /usr/local/bin/pdb_variants
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structure_info

```bash
$ singularity exec <container> /usr/local/bin/structure_info
$ podman run --it --rm --entrypoint /usr/local/bin/structure_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structure_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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