
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bibliotheques`
--

CREATE TABLE `objets_reservables` (
  `id_objet_reservable` int(11) NOT NULL AUTO_INCREMENT,
  `type_objet_reservable` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `objets_reservables`
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


CREATE TABLE `ressources_externes` (
  `id_objet_reservable` int(11) NOT NULL,
  `nom_ressource` varchar(50) DEFAULT NULL,
  `etat_ressource` tinyint(1) DEFAULT NULL,
  `disponibilite` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `ressources_internes` (
  `id_objet_reservable` int(11) NOT NULL,
  `nom_ressource` varchar(50) DEFAULT NULL,
  `id_espace_actuel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE `utilisateurs` (
  `id_utilisateur` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(15) DEFAULT NULL,
  `prenom` varchar(15) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `mdp` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `eleves` (
  `id_utilisateur` int(11) NOT NULL,
  `promotion` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `enseignants` (
  `id_utilisateur` int(11) NOT NULL,
  `matiere` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--

CREATE TABLE `administrateurs` (
  `id_utilisateur` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `administrateurs`
--





CREATE TABLE `reserver` (
  `id_reservation` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  `duree` int(11) DEFAULT NULL,
  `nb_pers` int(11) DEFAULT NULL,
  `id_objet_reservable` int(11) DEFAULT NULL,
  `id_utilisateur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



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


INSERT INTO `objets_reservables` (`id_objet_reservable`, `type_objet_reservable`) VALUES
('Alcove'),
('Alcove'),
('Alcove'),
('Alcove'),
('Alcove'),
('Click-share'),
('Stylet pour Surface Hub'),
('Stylet pour Surface Hub');



INSERT INTO `alcove` (`id_objet_reservable`, `nom_ville`, `couleur`, `disponibilite`, `nb_places`, `id_espace_actuel`, `nom_continent`) VALUES
('Toulouse', 'gris', 1, 10, 1, 'Europe'),
('Abidjan', 'rouge', 1, 10, 2, 'Afrique'),
('Brasilia', 'jaune', 1, 10, 3, 'Amérique'),
('Tiajin', 'vert', 1, 6, 4, 'Asie'),
('Nouméa', 'bleu', 1, 10, 5, 'Océanie');


INSERT INTO `utilisateurs` (`id_utilisateur`, `nom`, `prenom`, `mail`, `mdp`) VALUES
('Louli', 'Danyl', 'danyl.louli@alumni.enac.fr', 'azerty'),
('Leclercq', 'Antoine', 'antoine.leclercq@alumni.enac.fr', 'toto'),
('Dubois', 'Loic', 'loic.dubois@alumni.enac.fr', 'PSGchampions'),
('Antona', 'Clotilde', 'clotilde.antona@alumni.enac.fr', 'Vertmeilleurecouleur'),
('Lezaud', 'Pascal', 'Pascal.lezaud@enac.fr', 'analyse'),
('Porte', 'Laurence', 'Laurence.porte@enac.fr', 'analyse');

INSERT INTO `eleves` (`id_utilisateur`, `promotion`) VALUES
('IENAC18'),
('IENAC18'),
('IENAC18'),
('IENAC18');


INSERT INTO `administrateurs` () VALUES
();

INSERT INTO `enseignants` (`id_utilisateur`, `matiere`) VALUES
('Théorie de la mesure');

INSERT INTO `reserver` (`id_reservation`, `date`, `heure`, `duree`, `nb_pers`, `id_objet_reservable`, `id_utilisateur`) VALUES
('2019-04-29', '08:00:00', 90, 4, 3, 1);



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
