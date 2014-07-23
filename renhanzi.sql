
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `renhanzi`
--

-- --------------------------------------------------------

--
-- Table structure for table `dic_content`
--

CREATE TABLE IF NOT EXISTS `dic_content` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `hanzi` varchar(1) NOT NULL DEFAULT ' ',
  `wubi` varchar(10) DEFAULT NULL,
  `radical` varchar(10) NOT NULL,
  `num` tinyint(2) NOT NULL DEFAULT '0',
  `main_num` varchar(2) NOT NULL DEFAULT '0',
  `pronunciation` varchar(50) NOT NULL DEFAULT '',
  `summary` text,
  `content` longtext,
  `hits` int(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `hanzi` (`hanzi`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=20903 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_hanzi`
--

CREATE TABLE IF NOT EXISTS `dic_hanzi` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `hanzi` varchar(10) NOT NULL DEFAULT '',
  `pinyin` varchar(10) NOT NULL DEFAULT '',
  `num` tinyint(2) NOT NULL DEFAULT '0',
  `main_num` varchar(2) NOT NULL DEFAULT '',
  `radical` varchar(10) NOT NULL DEFAULT '',
  `radical_num` tinyint(2) NOT NULL DEFAULT '0',
  `status` varchar(20) NOT NULL DEFAULT 'publish',
  PRIMARY KEY (`id`),
  KEY `hanzi` (`hanzi`),
  KEY `pinyin` (`pinyin`),
  KEY `num` (`num`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=23992 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_idiom`
--

CREATE TABLE IF NOT EXISTS `dic_idiom` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `hanzi` varchar(1) NOT NULL DEFAULT '',
  `idiom` varchar(255) DEFAULT NULL,
  `pinyin` varchar(255) DEFAULT NULL,
  `abc` varchar(20) DEFAULT NULL,
  `difficulty` varchar(20) DEFAULT NULL,
  `description` longtext,
  `source` longtext,
  `example` longtext,
  `synonyms` text,
  `antonym` text,
  `instructions` longtext,
  `english` longtext,
  `story` longtext,
  `hits` int(20) NOT NULL DEFAULT '0',
  `status` varchar(20) NOT NULL DEFAULT 'publish',
  PRIMARY KEY (`id`),
  KEY `hanzi` (`hanzi`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13301 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_pinyin`
--

CREATE TABLE IF NOT EXISTS `dic_pinyin` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `slug` varchar(1) NOT NULL DEFAULT '',
  `pinyin` varchar(10) NOT NULL DEFAULT '',
  `sort` tinyint(3) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=412 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_pronunciation`
--

CREATE TABLE IF NOT EXISTS `dic_pronunciation` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `hanzi` varchar(10) NOT NULL DEFAULT '',
  `pinyin` varchar(10) NOT NULL DEFAULT '',
  `pronunciation` varchar(10) NOT NULL DEFAULT '',
  `tone` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `pronunciation` (`pronunciation`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34084 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_radical`
--

CREATE TABLE IF NOT EXISTS `dic_radical` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `radical` varchar(3) NOT NULL DEFAULT '',
  `num` tinyint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=271 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_sandt`
--

CREATE TABLE IF NOT EXISTS `dic_sandt` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `simplified` varchar(1) NOT NULL DEFAULT '',
  `traditional` varchar(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2192 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_tone`
--

CREATE TABLE IF NOT EXISTS `dic_tone` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `pinyin` varchar(10) NOT NULL DEFAULT '',
  `pronunciation` varchar(10) NOT NULL DEFAULT '',
  `tone` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `pronunciation` (`pronunciation`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2046 ;

-- --------------------------------------------------------

--
-- Table structure for table `dic_word`
--

CREATE TABLE IF NOT EXISTS `dic_word` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `hanzi` varchar(1) NOT NULL DEFAULT ' ',
  `word` varchar(50) NOT NULL,
  `description` longtext,
  `traditional` varchar(50) DEFAULT NULL,
  `pinyin` varchar(50) DEFAULT NULL,
  `hits` int(20) NOT NULL DEFAULT '0',
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hanzi` (`hanzi`),
  KEY `word` (`word`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=371773 ;

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
