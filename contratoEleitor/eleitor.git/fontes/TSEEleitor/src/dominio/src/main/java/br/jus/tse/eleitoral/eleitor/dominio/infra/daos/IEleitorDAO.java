package br.jus.tse.eleitoral.eleitor.dominio.infra.daos;

import java.util.List;

import br.jus.tse.corporativa.arqjeespring.infra.daos.IBaseCRUDDAO;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;

public interface IEleitorDAO extends IBaseCRUDDAO<Eleitor, String> {

	public Eleitor findByNumeroInscricao(String pNumInscricao) throws DBAcessoDadosException;
	
	
	public List<Eleitor> findByDadosEspecialissimos(String inscricao, 
													Integer dataNascimento, 
													String nome, 
													String nomePai, 
													String nomeMae) 
		throws DBAcessoDadosException;
	

	public Eleitor findByNumeroInscricaoDataNascimentoNomeMaeLimpo(String inscricao, 
																   Integer dataNascimento, 
																   String nomeMaeLimpo) 
		throws DBAcessoDadosException;
	

	public Eleitor findByNomeDataNascimentoNomeMaeLimpo(String nome, 
														Integer dataNascimento, 
														String nomeMaeLimpo) 
		throws DBAcessoDadosException;
	
}
