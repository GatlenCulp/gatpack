{
  description = "A PDF and website templating tool (Note: Flake may not be functional)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    nix-bundle.url = "github:matthewbauer/nix-bundle";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      nix-bundle,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages = rec {
          gatpack = pkgs.callPackage ./default.nix { };
          default = gatpack;
          bundle = nix-bundle.bundlers.${system}.bundle self.packages.${system}.default;
        };

        apps = rec {
          gatpack = flake-utils.lib.mkApp { drv = self.packages.${system}.gatpack; };
          default = gatpack;
        };
      }
    );
}
