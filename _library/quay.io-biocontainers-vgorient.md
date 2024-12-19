---
layout: container
name:  "quay.io/biocontainers/vgorient"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vgorient/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vgorient/container.yaml"
updated_at: "2024-12-19 04:29:35.812140"
latest: "0.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vgorient"
aliases:
 - "Cutoff_Node.py"
 - "OOP_gfa_parser.py"
 - "Rotation_and_Orientation.py"
 - "VG_diterative.py"
 - "VG_iterative.py"
 - "cut_and_rot.py"
 - "cut_and_rot_orient.py"
 - "cut_and_rot_rebuild.py"
 - "jaccard_dit_wrapper.py"
 - "kmer_jaccard.py"
 - "kmer_rotation_multiprocessing.py"
 - "noisify.py"
 - "offset_fasta.py"
 - "request_fastas.py"
 - "vg"
 - "numpy-config"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
versions:
 - "0.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for vgorient"
config: {"url": "https://biocontainers.pro/tools/vgorient", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vgorient", "latest": {"0.1.1--pyhdfd78af_0": "sha256:83018694cb3d1f94625259f7d559c84885798b2ce31b857800d431e48af3c867"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:83018694cb3d1f94625259f7d559c84885798b2ce31b857800d431e48af3c867"}, "docker": "quay.io/biocontainers/vgorient", "aliases": {"Cutoff_Node.py": "/usr/local/bin/Cutoff_Node.py", "OOP_gfa_parser.py": "/usr/local/bin/OOP_gfa_parser.py", "Rotation_and_Orientation.py": "/usr/local/bin/Rotation_and_Orientation.py", "VG_diterative.py": "/usr/local/bin/VG_diterative.py", "VG_iterative.py": "/usr/local/bin/VG_iterative.py", "cut_and_rot.py": "/usr/local/bin/cut_and_rot.py", "cut_and_rot_orient.py": "/usr/local/bin/cut_and_rot_orient.py", "cut_and_rot_rebuild.py": "/usr/local/bin/cut_and_rot_rebuild.py", "jaccard_dit_wrapper.py": "/usr/local/bin/jaccard_dit_wrapper.py", "kmer_jaccard.py": "/usr/local/bin/kmer_jaccard.py", "kmer_rotation_multiprocessing.py": "/usr/local/bin/kmer_rotation_multiprocessing.py", "noisify.py": "/usr/local/bin/noisify.py", "offset_fasta.py": "/usr/local/bin/offset_fasta.py", "request_fastas.py": "/usr/local/bin/request_fastas.py", "vg": "/usr/local/bin/vg", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vgorient.
singularity registry hpc automated addition for vgorient
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vgorient
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vgorient:0.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vgorient/0.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/vgorient/0.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vgorient-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vgorient-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vgorient-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vgorient-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vgorient-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vgorient-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cutoff_Node.py

```bash
$ singularity exec <container> /usr/local/bin/Cutoff_Node.py
$ podman run --it --rm --entrypoint /usr/local/bin/Cutoff_Node.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Cutoff_Node.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### OOP_gfa_parser.py

```bash
$ singularity exec <container> /usr/local/bin/OOP_gfa_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/OOP_gfa_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/OOP_gfa_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rotation_and_Orientation.py

```bash
$ singularity exec <container> /usr/local/bin/Rotation_and_Orientation.py
$ podman run --it --rm --entrypoint /usr/local/bin/Rotation_and_Orientation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rotation_and_Orientation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VG_diterative.py

```bash
$ singularity exec <container> /usr/local/bin/VG_diterative.py
$ podman run --it --rm --entrypoint /usr/local/bin/VG_diterative.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VG_diterative.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VG_iterative.py

```bash
$ singularity exec <container> /usr/local/bin/VG_iterative.py
$ podman run --it --rm --entrypoint /usr/local/bin/VG_iterative.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VG_iterative.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_and_rot.py

```bash
$ singularity exec <container> /usr/local/bin/cut_and_rot.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_and_rot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_and_rot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_and_rot_orient.py

```bash
$ singularity exec <container> /usr/local/bin/cut_and_rot_orient.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_and_rot_orient.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_and_rot_orient.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_and_rot_rebuild.py

```bash
$ singularity exec <container> /usr/local/bin/cut_and_rot_rebuild.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_and_rot_rebuild.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_and_rot_rebuild.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaccard_dit_wrapper.py

```bash
$ singularity exec <container> /usr/local/bin/jaccard_dit_wrapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/jaccard_dit_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaccard_dit_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_jaccard.py

```bash
$ singularity exec <container> /usr/local/bin/kmer_jaccard.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_jaccard.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_jaccard.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_rotation_multiprocessing.py

```bash
$ singularity exec <container> /usr/local/bin/kmer_rotation_multiprocessing.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_rotation_multiprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_rotation_multiprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### noisify.py

```bash
$ singularity exec <container> /usr/local/bin/noisify.py
$ podman run --it --rm --entrypoint /usr/local/bin/noisify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/noisify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### offset_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/offset_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/offset_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/offset_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### request_fastas.py

```bash
$ singularity exec <container> /usr/local/bin/request_fastas.py
$ podman run --it --rm --entrypoint /usr/local/bin/request_fastas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/request_fastas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vg

```bash
$ singularity exec <container> /usr/local/bin/vg
$ podman run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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