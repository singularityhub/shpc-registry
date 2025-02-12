---
layout: container
name:  "quay.io/biocontainers/vvv2_display"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vvv2_display/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vvv2_display/container.yaml"
updated_at: "2025-02-12 03:00:23.118760"
latest: "0.2.3.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vvv2_display"
aliases:
 - "convert_tbl2json.py"
 - "convert_vcffile_to_readablefile2.py"
 - "correct_covdepth_f.py"
 - "correct_multicontig_vardict_vcf.py"
 - "visualize_coverage_depth.R"
 - "visualize_snp_v4.R"
 - "vvv2_display.py"
 - "hb-info"
 - "tjbench"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.2.3.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for vvv2_display"
config: {"url": "https://biocontainers.pro/tools/vvv2_display", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vvv2_display", "latest": {"0.2.3.3--pyhdfd78af_0": "sha256:1499bdd3ac6aa2894a35a234f1a5ccdd621fd7d05ed416ee4b4defa05202da99"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:8dee685ecc5e356091ac3de6c40f8f7d35461b99c0cff682245c794068ad3221", "0.2.2--pyhdfd78af_0": "sha256:6240714d3065bae647ca5ea3af049c1125d9eb3a2c949b595467b37f031636da", "0.2.3.3--pyhdfd78af_0": "sha256:1499bdd3ac6aa2894a35a234f1a5ccdd621fd7d05ed416ee4b4defa05202da99"}, "docker": "quay.io/biocontainers/vvv2_display", "aliases": {"convert_tbl2json.py": "/usr/local/bin/convert_tbl2json.py", "convert_vcffile_to_readablefile2.py": "/usr/local/bin/convert_vcffile_to_readablefile2.py", "correct_covdepth_f.py": "/usr/local/bin/correct_covdepth_f.py", "correct_multicontig_vardict_vcf.py": "/usr/local/bin/correct_multicontig_vardict_vcf.py", "visualize_coverage_depth.R": "/usr/local/bin/visualize_coverage_depth.R", "visualize_snp_v4.R": "/usr/local/bin/visualize_snp_v4.R", "vvv2_display.py": "/usr/local/bin/vvv2_display.py", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vvv2_display.
singularity registry hpc automated addition for vvv2_display
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vvv2_display
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vvv2_display:0.2.3.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vvv2_display/0.2.3.3--pyhdfd78af_0
$ module help quay.io/biocontainers/vvv2_display/0.2.3.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vvv2_display-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vvv2_display-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vvv2_display-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vvv2_display-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vvv2_display-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vvv2_display-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_tbl2json.py

```bash
$ singularity exec <container> /usr/local/bin/convert_tbl2json.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_tbl2json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_tbl2json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_vcffile_to_readablefile2.py

```bash
$ singularity exec <container> /usr/local/bin/convert_vcffile_to_readablefile2.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_vcffile_to_readablefile2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_vcffile_to_readablefile2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_covdepth_f.py

```bash
$ singularity exec <container> /usr/local/bin/correct_covdepth_f.py
$ podman run --it --rm --entrypoint /usr/local/bin/correct_covdepth_f.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_covdepth_f.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_multicontig_vardict_vcf.py

```bash
$ singularity exec <container> /usr/local/bin/correct_multicontig_vardict_vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/correct_multicontig_vardict_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_multicontig_vardict_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize_coverage_depth.R

```bash
$ singularity exec <container> /usr/local/bin/visualize_coverage_depth.R
$ podman run --it --rm --entrypoint /usr/local/bin/visualize_coverage_depth.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize_coverage_depth.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize_snp_v4.R

```bash
$ singularity exec <container> /usr/local/bin/visualize_snp_v4.R
$ podman run --it --rm --entrypoint /usr/local/bin/visualize_snp_v4.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize_snp_v4.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vvv2_display.py

```bash
$ singularity exec <container> /usr/local/bin/vvv2_display.py
$ podman run --it --rm --entrypoint /usr/local/bin/vvv2_display.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vvv2_display.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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