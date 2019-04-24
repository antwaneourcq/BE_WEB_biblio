-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mar. 23 avr. 2019 à 13:38
-- Version du serveur :  10.1.38-MariaDB
-- Version de PHP :  7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bibliotheque`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateurs`
--

CREATE TABLE `administrateurs` (
  `id_utilisateur` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `administrateurs`
--

INSERT INTO `administrateurs` (`id_utilisateur`) VALUES
(6);

-- --------------------------------------------------------

--
-- Structure de la table `alcove`
--

CREATE TABLE `alcove` (
  `id_objet_reservable` int(11) NOT NULL,
  `nom_ville` varchar(20) DEFAULT NULL,
  `couleur` varchar(15) DEFAULT NULL,
  `disponibilite` tinyint(1) DEFAULT NULL,
  `nb_places` int(11) NOT NULL,
  `id_espace_actuel` int(11) NOT NULL,
  `nom_continent` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `alcove`
--

INSERT INTO `alcove` (`id_objet_reservable`, `nom_ville`, `couleur`, `disponibilite`, `nb_places`, `id_espace_actuel`, `nom_continent`) VALUES
(1, 'Toulouse', 'gris', 1, 10, 1, 'Europe'),
(2, 'Abidjan', 'rouge', 1, 10, 2, 'Afrique'),
(3, 'Brasilia', 'jaune', 1, 10, 3, 'Amérique'),
(4, 'Tiajin', 'vert', 1, 6, 4, 'Asie'),
(5, 'Nouméa', 'bleu', 1, 10, 5, 'Océanie');

-- --------------------------------------------------------

--
-- Structure de la table `eleves`
--

CREATE TABLE `eleves` (
  `id_utilisateur` int(11) NOT NULL,
  `promotion` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `eleves`
--

INSERT INTO `eleves` (`id_utilisateur`, `promotion`) VALUES
(1, 'IENAC18'),
(2, 'IENAC18'),
(3, 'IENAC18'),
(4, 'IENAC18');

-- --------------------------------------------------------

--
-- Structure de la table `enseignants`
--

CREATE TABLE `enseignants` (
  `id_utilisateur` int(11) NOT NULL,
  `matiere` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `enseignants`
--

INSERT INTO `enseignants` (`id_utilisateur`, `matiere`) VALUES
(6, 'Théorie de la mesure');

-- --------------------------------------------------------

--
-- Structure de la table `objets_reservables`
--

CREATE TABLE `objets_reservables` (
  `id_objet_reservable` int(11) NOT NULL,
  `type_objet_reservable` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `objets_reservables`
--

INSERT INTO `objets_reservables` (`id_objet_reservable`, `type_objet_reservable`) VALUES
(1, 'Alcove'),
(2, 'Alcove'),
(3, 'Alcove'),
(4, 'Alcove'),
(5, 'Alcove'),
(6, 'Click-share'),
(7, 'Stylet pour Surface Hub'),
(8, 'Stylet pour Surface Hub');

-- --------------------------------------------------------

--
-- Structure de la table `reserver`
--

CREATE TABLE `reserver` (
  `id_reservation` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  `duree` int(11) DEFAULT NULL,
  `nb_pers` int(11) DEFAULT NULL,
  `id_objet_reservable` int(11) DEFAULT NULL,
  `id_utilisateur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `reserver`
--

INSERT INTO `reserver` (`id_reservation`, `date`, `heure`, `duree`, `nb_pers`, `id_objet_reservable`, `id_utilisateur`) VALUES
(1, '2019-04-29', '08:00:00', 90, 4, 3, 1);

-- --------------------------------------------------------

--
-- Structure de la table `ressources_externes`
--

CREATE TABLE `ressources_externes` (
  `id_objet_reservable` int(11) NOT NULL,
  `nom_ressource` varchar(50) DEFAULT NULL,
  `etat_ressource` tinyint(1) DEFAULT NULL,
  `disponibilite` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `ressources_internes`
--

CREATE TABLE `ressources_internes` (
  `id_objet_reservable` int(11) NOT NULL,
  `nom_ressource` varchar(50) DEFAULT NULL,
  `id_espace_actuel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id_utilisateur` int(11) NOT NULL,
  `nom` varchar(15) DEFAULT NULL,
  `prenom` varchar(15) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `mdp` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id_utilisateur`, `nom`, `prenom`, `mail`, `mdp`) VALUES
(1, 'Louli', 'Danyl', 'danyl.louli@alumni.enac.fr', 'azerty'),
(2, 'Leclercq', 'Antoine', 'antoine.leclercq@alumni.enac.fr', 'toto'),
(3, 'Dubois', 'Loic', 'loic.dubois@alumni.enac.fr', 'PSGchampions'),
(4, 'Antona', 'Clotilde', 'clotilde.antona@alumni.enac.fr', 'Vertmeilleurecouleur'),
(5, 'Lezaud', 'Pascal', 'Pascal.lezaud@enac.fr', 'analyse'),
(6, 'Porte', 'Laurence', 'Laurence.porte@enac.fr', 'analyse');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD PRIMARY KEY (`id_utilisateur`);

--
-- Index pour la table `alcove`
--
ALTER TABLE `alcove`
  ADD PRIMARY KEY (`id_objet_reservable`);

--
-- Index pour la table `eleves`
--
ALTER TABLE `eleves`
  ADD PRIMARY KEY (`id_utilisateur`);

--
-- Index pour la table `enseignants`
--
ALTER TABLE `enseignants`
  ADD PRIMARY KEY (`id_utilisateur`);

--
-- Index pour la table `objets_reservables`
--
ALTER TABLE `objets_reservables`
  ADD PRIMARY KEY (`id_objet_reservable`);

--
-- Index pour la table `reserver`
--
ALTER TABLE `reserver`
  ADD PRIMARY KEY (`id_reservation`),
  ADD KEY `id_objet_reservable` (`id_objet_reservable`),
  ADD KEY `id_utilisateur` (`id_utilisateur`);

--
-- Index pour la table `ressources_externes`
--
ALTER TABLE `ressources_externes`
  ADD PRIMARY KEY (`id_objet_reservable`);

--
-- Index pour la table `ressources_internes`
--
ALTER TABLE `ressources_internes`
  ADD PRIMARY KEY (`id_objet_reservable`);

--
-- Index pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id_utilisateur`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD CONSTRAINT `administrateurs_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `alcove`
--
ALTER TABLE `alcove`
  ADD CONSTRAINT `alcove_ibfk_1` FOREIGN KEY (`id_objet_reservable`) REFERENCES `objets_reservables` (`id_objet_reservable`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `eleves`
--
ALTER TABLE `eleves`
  ADD CONSTRAINT `eleves_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `enseignants`
--
ALTER TABLE `enseignants`
  ADD CONSTRAINT `enseignants_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `reserver`
--
ALTER TABLE `reserver`
  ADD CONSTRAINT `reserver_ibfk_1` FOREIGN KEY (`id_objet_reservable`) REFERENCES `objets_reservables` (`id_objet_reservable`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reserver_ibfk_2` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `ressources_externes`
--
ALTER TABLE `ressources_externes`
  ADD CONSTRAINT `ressources_externes_ibfk_1` FOREIGN KEY (`id_objet_reservable`) REFERENCES `objets_reservables` (`id_objet_reservable`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
