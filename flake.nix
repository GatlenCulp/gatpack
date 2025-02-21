{
  description = "A PDF and website templating tool";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
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
        };

        apps = rec {
          gatpack = flake-utils.lib.mkApp { drv = self.packages.${system}.gatpack; };
          default = gatpack;
        };
      }
    );
}
