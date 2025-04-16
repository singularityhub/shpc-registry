---
layout: container
name:  "quay.io/biocontainers/splash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splash/container.yaml"
updated_at: "2025-04-16 04:54:42.829718"
latest: "2.11.0--py313h9ee0642_0"
container_url: "https://biocontainers.pro/tools/splash"
aliases:
 - "bkc"
 - "bkc_dump"
 - "build_lookup_table.py"
 - "compactors"
 - "dsv_manip"
 - "fafq_filter"
 - "gap_shortener"
 - "idle3.13"
 - "lookup_table"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "read_selector"
 - "satc"
 - "satc_dump"
 - "satc_filter"
 - "satc_merge"
 - "satc_to_fasta"
 - "satc_undump"
 - "sig_anch"
 - "splash"
 - "supervised_test.R"
 - "tsv_to_fasta"
 - "kmc"
 - "kmc_tools"
 - "metadata_conda_debug.yaml"
 - "build_env_setup.sh"
 - "conda_build.sh"
versions:
 - "2.11.0--py313h9ee0642_0"
description: "singularity registry hpc automated addition for splash"
config: {"url": "https://biocontainers.pro/tools/splash", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for splash", "latest": {"2.11.0--py313h9ee0642_0": "sha256:7a65568e7d34aa4fe0a18f0adc0a1bc49d2361e24684bb2e1a47802364800043"}, "tags": {"2.11.0--py313h9ee0642_0": "sha256:7a65568e7d34aa4fe0a18f0adc0a1bc49d2361e24684bb2e1a47802364800043"}, "docker": "quay.io/biocontainers/splash", "aliases": {"bkc": "/usr/local/bin/bkc", "bkc_dump": "/usr/local/bin/bkc_dump", "build_lookup_table.py": "/usr/local/bin/build_lookup_table.py", "compactors": "/usr/local/bin/compactors", "dsv_manip": "/usr/local/bin/dsv_manip", "fafq_filter": "/usr/local/bin/fafq_filter", "gap_shortener": "/usr/local/bin/gap_shortener", "idle3.13": "/usr/local/bin/idle3.13", "lookup_table": "/usr/local/bin/lookup_table", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "read_selector": "/usr/local/bin/read_selector", "satc": "/usr/local/bin/satc", "satc_dump": "/usr/local/bin/satc_dump", "satc_filter": "/usr/local/bin/satc_filter", "satc_merge": "/usr/local/bin/satc_merge", "satc_to_fasta": "/usr/local/bin/satc_to_fasta", "satc_undump": "/usr/local/bin/satc_undump", "sig_anch": "/usr/local/bin/sig_anch", "splash": "/usr/local/bin/splash", "supervised_test.R": "/usr/local/bin/supervised_test.R", "tsv_to_fasta": "/usr/local/bin/tsv_to_fasta", "kmc": "/usr/local/bin/kmc", "kmc_tools": "/usr/local/bin/kmc_tools", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splash.
singularity registry hpc automated addition for splash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splash:2.11.0--py313h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splash/2.11.0--py313h9ee0642_0
$ module help quay.io/biocontainers/splash/2.11.0--py313h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bkc

```bash
$ singularity exec <container> /usr/local/bin/bkc
$ podman run --it --rm --entrypoint /usr/local/bin/bkc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bkc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bkc_dump

```bash
$ singularity exec <container> /usr/local/bin/bkc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/bkc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bkc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_lookup_table.py

```bash
$ singularity exec <container> /usr/local/bin/build_lookup_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/build_lookup_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_lookup_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compactors

```bash
$ singularity exec <container> /usr/local/bin/compactors
$ podman run --it --rm --entrypoint /usr/local/bin/compactors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compactors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsv_manip

```bash
$ singularity exec <container> /usr/local/bin/dsv_manip
$ podman run --it --rm --entrypoint /usr/local/bin/dsv_manip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsv_manip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fafq_filter

```bash
$ singularity exec <container> /usr/local/bin/fafq_filter
$ podman run --it --rm --entrypoint /usr/local/bin/fafq_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fafq_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gap_shortener

```bash
$ singularity exec <container> /usr/local/bin/gap_shortener
$ podman run --it --rm --entrypoint /usr/local/bin/gap_shortener   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gap_shortener   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lookup_table

```bash
$ singularity exec <container> /usr/local/bin/lookup_table
$ podman run --it --rm --entrypoint /usr/local/bin/lookup_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lookup_table   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### read_selector

```bash
$ singularity exec <container> /usr/local/bin/read_selector
$ podman run --it --rm --entrypoint /usr/local/bin/read_selector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_selector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc

```bash
$ singularity exec <container> /usr/local/bin/satc
$ podman run --it --rm --entrypoint /usr/local/bin/satc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc_dump

```bash
$ singularity exec <container> /usr/local/bin/satc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/satc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc_filter

```bash
$ singularity exec <container> /usr/local/bin/satc_filter
$ podman run --it --rm --entrypoint /usr/local/bin/satc_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc_merge

```bash
$ singularity exec <container> /usr/local/bin/satc_merge
$ podman run --it --rm --entrypoint /usr/local/bin/satc_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/satc_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/satc_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satc_undump

```bash
$ singularity exec <container> /usr/local/bin/satc_undump
$ podman run --it --rm --entrypoint /usr/local/bin/satc_undump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satc_undump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sig_anch

```bash
$ singularity exec <container> /usr/local/bin/sig_anch
$ podman run --it --rm --entrypoint /usr/local/bin/sig_anch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sig_anch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splash

```bash
$ singularity exec <container> /usr/local/bin/splash
$ podman run --it --rm --entrypoint /usr/local/bin/splash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### supervised_test.R

```bash
$ singularity exec <container> /usr/local/bin/supervised_test.R
$ podman run --it --rm --entrypoint /usr/local/bin/supervised_test.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/supervised_test.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/tsv_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/tsv_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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