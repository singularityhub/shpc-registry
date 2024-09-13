---
layout: container
name:  "quay.io/biocontainers/md-cogent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/md-cogent/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/md-cogent/container.yaml"
updated_at: "2024-09-13 03:24:41.315271"
latest: "8.0.0--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/md-cogent"
aliases:
 - "generate_batch_cmd_for_Cogent_family_finding.py"
 - "generate_batch_cmd_for_Cogent_reconstruction.py"
 - "gff3_to_collapsed.py"
 - "process_kmer_to_graph.py"
 - "reconstruct_contig.py"
 - "run_mash.py"
 - "JxrDecApp"
 - "JxrEncApp"
 - "cbrunsli"
 - "dbrunsli"
 - "imagecodecs"
 - "lsm2bin"
 - "tifffile"
 - "zfp"
 - "zopfli"
 - "zopflipng"
versions:
 - "8.0.0--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for md-cogent"
config: {"url": "https://biocontainers.pro/tools/md-cogent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for md-cogent", "latest": {"8.0.0--pyh3252c3a_0": "sha256:f781f46643b49112636f3c3cb4b9c7848549ed540880eccb7f9f85d753e10e3a"}, "tags": {"8.0.0--pyh3252c3a_0": "sha256:f781f46643b49112636f3c3cb4b9c7848549ed540880eccb7f9f85d753e10e3a"}, "docker": "quay.io/biocontainers/md-cogent", "aliases": {"generate_batch_cmd_for_Cogent_family_finding.py": "/usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py", "generate_batch_cmd_for_Cogent_reconstruction.py": "/usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py", "gff3_to_collapsed.py": "/usr/local/bin/gff3_to_collapsed.py", "process_kmer_to_graph.py": "/usr/local/bin/process_kmer_to_graph.py", "reconstruct_contig.py": "/usr/local/bin/reconstruct_contig.py", "run_mash.py": "/usr/local/bin/run_mash.py", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/md-cogent.
shpc-registry automated BioContainers addition for md-cogent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/md-cogent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/md-cogent:8.0.0--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/md-cogent/8.0.0--pyh3252c3a_0
$ module help quay.io/biocontainers/md-cogent/8.0.0--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### md-cogent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### md-cogent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### md-cogent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### md-cogent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### md-cogent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### md-cogent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### generate_batch_cmd_for_Cogent_family_finding.py

```bash
$ singularity exec <container> /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_batch_cmd_for_Cogent_reconstruction.py

```bash
$ singularity exec <container> /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_to_collapsed.py

```bash
$ singularity exec <container> /usr/local/bin/gff3_to_collapsed.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_to_collapsed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_to_collapsed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_kmer_to_graph.py

```bash
$ singularity exec <container> /usr/local/bin/process_kmer_to_graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/process_kmer_to_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_kmer_to_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reconstruct_contig.py

```bash
$ singularity exec <container> /usr/local/bin/reconstruct_contig.py
$ podman run --it --rm --entrypoint /usr/local/bin/reconstruct_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reconstruct_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mash.py

```bash
$ singularity exec <container> /usr/local/bin/run_mash.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagecodecs

```bash
$ singularity exec <container> /usr/local/bin/imagecodecs
$ podman run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsm2bin

```bash
$ singularity exec <container> /usr/local/bin/lsm2bin
$ podman run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tifffile

```bash
$ singularity exec <container> /usr/local/bin/tifffile
$ podman run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfp

```bash
$ singularity exec <container> /usr/local/bin/zfp
$ podman run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopfli

```bash
$ singularity exec <container> /usr/local/bin/zopfli
$ podman run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopflipng

```bash
$ singularity exec <container> /usr/local/bin/zopflipng
$ podman run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
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