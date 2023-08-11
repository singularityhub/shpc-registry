---
layout: container
name:  "quay.io/biocontainers/biobb_structure_utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_structure_utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_structure_utils/container.yaml"
updated_at: "2023-08-11 02:43:55.390643"
latest: "4.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_structure_utils"
aliases:
 - "cat_pdb"
 - "check_structure"
 - "closest_residues"
 - "extract_atoms"
 - "extract_chain"
 - "extract_heteroatoms"
 - "extract_model"
 - "extract_molecule"
 - "extract_residues"
 - "remove_ligand"
 - "remove_molecules"
 - "remove_pdb_water"
 - "renumber_structure"
 - "sort_gro_residues"
 - "str_check_add_hydrogens"
 - "structure_check"
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
description: "shpc-registry automated BioContainers addition for biobb_structure_utils"
config: {"url": "https://biocontainers.pro/tools/biobb_structure_utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_structure_utils", "latest": {"4.0.0--pyhdfd78af_0": "sha256:7c53d46011e412cfb42c3e8fa40c62cca095e67aaf2bd26687893e60c80da795"}, "tags": {"3.8.0--pyhdfd78af_0": "sha256:51b2293c73481b53133b9386e234c1981e801442dea810147adf34455351a38e", "3.9.0--pyhdfd78af_0": "sha256:f747b7e6e1219f90b783452b3d624ca43c2f061b2b263624ea0de3832efcb411", "4.0.0--pyhdfd78af_0": "sha256:7c53d46011e412cfb42c3e8fa40c62cca095e67aaf2bd26687893e60c80da795"}, "docker": "quay.io/biocontainers/biobb_structure_utils", "aliases": {"cat_pdb": "/usr/local/bin/cat_pdb", "check_structure": "/usr/local/bin/check_structure", "closest_residues": "/usr/local/bin/closest_residues", "extract_atoms": "/usr/local/bin/extract_atoms", "extract_chain": "/usr/local/bin/extract_chain", "extract_heteroatoms": "/usr/local/bin/extract_heteroatoms", "extract_model": "/usr/local/bin/extract_model", "extract_molecule": "/usr/local/bin/extract_molecule", "extract_residues": "/usr/local/bin/extract_residues", "remove_ligand": "/usr/local/bin/remove_ligand", "remove_molecules": "/usr/local/bin/remove_molecules", "remove_pdb_water": "/usr/local/bin/remove_pdb_water", "renumber_structure": "/usr/local/bin/renumber_structure", "sort_gro_residues": "/usr/local/bin/sort_gro_residues", "str_check_add_hydrogens": "/usr/local/bin/str_check_add_hydrogens", "structure_check": "/usr/local/bin/structure_check", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_structure_utils.
shpc-registry automated BioContainers addition for biobb_structure_utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_structure_utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_structure_utils:4.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_structure_utils/4.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_structure_utils/4.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_structure_utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_structure_utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_structure_utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_structure_utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_structure_utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_structure_utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cat_pdb

```bash
$ singularity exec <container> /usr/local/bin/cat_pdb
$ podman run --it --rm --entrypoint /usr/local/bin/cat_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_structure

```bash
$ singularity exec <container> /usr/local/bin/check_structure
$ podman run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closest_residues

```bash
$ singularity exec <container> /usr/local/bin/closest_residues
$ podman run --it --rm --entrypoint /usr/local/bin/closest_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closest_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_atoms

```bash
$ singularity exec <container> /usr/local/bin/extract_atoms
$ podman run --it --rm --entrypoint /usr/local/bin/extract_atoms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_atoms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_chain

```bash
$ singularity exec <container> /usr/local/bin/extract_chain
$ podman run --it --rm --entrypoint /usr/local/bin/extract_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_heteroatoms

```bash
$ singularity exec <container> /usr/local/bin/extract_heteroatoms
$ podman run --it --rm --entrypoint /usr/local/bin/extract_heteroatoms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_heteroatoms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_model

```bash
$ singularity exec <container> /usr/local/bin/extract_model
$ podman run --it --rm --entrypoint /usr/local/bin/extract_model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_molecule

```bash
$ singularity exec <container> /usr/local/bin/extract_molecule
$ podman run --it --rm --entrypoint /usr/local/bin/extract_molecule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_molecule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_residues

```bash
$ singularity exec <container> /usr/local/bin/extract_residues
$ podman run --it --rm --entrypoint /usr/local/bin/extract_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_ligand

```bash
$ singularity exec <container> /usr/local/bin/remove_ligand
$ podman run --it --rm --entrypoint /usr/local/bin/remove_ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_ligand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_molecules

```bash
$ singularity exec <container> /usr/local/bin/remove_molecules
$ podman run --it --rm --entrypoint /usr/local/bin/remove_molecules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_molecules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_pdb_water

```bash
$ singularity exec <container> /usr/local/bin/remove_pdb_water
$ podman run --it --rm --entrypoint /usr/local/bin/remove_pdb_water   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_pdb_water   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renumber_structure

```bash
$ singularity exec <container> /usr/local/bin/renumber_structure
$ podman run --it --rm --entrypoint /usr/local/bin/renumber_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renumber_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_gro_residues

```bash
$ singularity exec <container> /usr/local/bin/sort_gro_residues
$ podman run --it --rm --entrypoint /usr/local/bin/sort_gro_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_gro_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### str_check_add_hydrogens

```bash
$ singularity exec <container> /usr/local/bin/str_check_add_hydrogens
$ podman run --it --rm --entrypoint /usr/local/bin/str_check_add_hydrogens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/str_check_add_hydrogens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structure_check

```bash
$ singularity exec <container> /usr/local/bin/structure_check
$ podman run --it --rm --entrypoint /usr/local/bin/structure_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structure_check   -v ${PWD} -w ${PWD} <container> -c " $@"
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